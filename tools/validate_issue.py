#!/usr/bin/env python3
"""Pre-publication validator for a brief issue.

Usage: python3 -I tools/validate_issue.py issues/YYYY-MM-DD.html

Exits non-zero if any BLOCKING check fails. Blocking checks are the ones
that have historically caught real defects before publication; advisory
checks print a warning and do not fail the run.

History of why each check exists is in config.md.
"""
import os
import re
import sys

BLOCK = []
WARN = []


def block(msg):
    BLOCK.append(msg)


def warn(msg):
    WARN.append(msg)


def main(path):
    s = open(path, encoding="utf-8").read()
    issue_dir = os.path.dirname(path)
    date = os.path.basename(path).replace(".html", "")

    # --- structural integrity -------------------------------------------
    ids = re.findall(r'<(?:article|details|h2)[^>]*\sid="([^"]+)"', s)
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        block(f"duplicate ids: {dupes}")

    anchors = set(re.findall(r'href="#([^"]+)"', s))
    missing = sorted(a for a in anchors if a not in ids)
    if missing:
        block(f"broken internal anchors: {missing}")

    for href in sorted(set(re.findall(r'href="(20\d\d-\d\d-\d\d\.html)(?:#([^"]*))?"', s))):
        target, frag = href if isinstance(href, tuple) else (href, "")
        tp = os.path.join(issue_dir, target)
        if not os.path.exists(tp):
            block(f"dead cross-issue link: {target}")
        elif frag:
            tids = re.findall(r'<(?:article|details|h2)[^>]*\sid="([^"]+)"', open(tp, encoding="utf-8").read())
            if frag not in tids:
                block(f"dead cross-issue anchor: {target}#{frag}")

    for tag in ("div", "article", "details", "figure", "section"):
        o = len(re.findall(rf"<{tag}[\s>]", s))
        c = len(re.findall(rf"</{tag}>", s))
        if o != c:
            block(f"tag mismatch <{tag}>: {o} open, {c} close")

    title = re.search(r"<title>(.*?)</title>", s)
    if not title:
        block("no <title>")
    elif date.replace("-", "") not in re.sub(r"\D", "", title.group(1)).replace("", ""):
        d = date.split("-")
        if not (d[2].lstrip("0") in title.group(1)):
            warn(f"title may carry the wrong date: {title.group(1)}")

    # --- divergence (added 4 Nov 2026 after nine issues carried none) ----
    div_boxes = len(re.findall(r'<div class="div">', s))
    leads = len(re.findall(r"<article id=", s))
    print(f"leads: {leads}   divergence boxes: {div_boxes}")
    if leads and div_boxes == 0:
        block(
            "NO DIVERGENCE BOXES. SKILL.md §6 requires one wherever sources genuinely "
            "disagree. Zero is permitted only if every lead is genuinely uncontested — "
            "which has been true on none of the days it was claimed."
        )

    # Buried divergence: phrases that signal a disagreement compressed into a clause.
    tells = [
        "can be read two ways", "read two ways", "two readings", "cuts both ways",
        "the question is whether", "either way", "it is equally consistent",
        "on the other hand", "a different reading",
    ]
    text = re.sub(r"<[^>]+>", " ", s).lower()
    found = sorted({t for t in tells if t in text})
    if found:
        # Only a problem if the phrase sits outside a divergence box.
        outside = []
        boxes = " ".join(re.findall(r'<div class="div">(.*?)</div>', s, re.S)).lower()
        boxes = re.sub(r"<[^>]+>", " ", boxes)
        for t in found:
            if text.count(t) > boxes.count(t):
                outside.append(t)
        if outside:
            block(f"buried divergence — these phrases appear outside any divergence box: {outside}")

    # --- house format ----------------------------------------------------
    shorts = re.findall(r'<details class="short" id="([^"]+)">(.*?)</details>', s, re.S)
    print(f"shorts: {len(shorts)}")
    if not shorts:
        block('no <details class="short"> items — wrong markup for the "Also today" tier')

    nav = len(re.findall(r'<nav[^>]*>.*?</nav>', s, re.S)) and len(
        re.findall(r'<li><a href="#', re.search(r"<nav[^>]*>(.*?)</nav>", s, re.S).group(1))
    )
    if nav and nav != leads + 1:
        block(f"nav has {nav} links for {leads} leads (expected {leads + 1} including Also today)")

    if "**" in re.sub(r"<[^>]+>", "", s):
        block("stray markdown asterisks in rendered text")
    if "<b></b>" in s:
        block("empty <b></b>")

    raw_amp = [
        m.start() for m in re.finditer(r"&(?!amp;|lt;|gt;|quot;|#\d+;|[a-zA-Z]+;)", s)
    ]
    script = {(m.start(), m.end()) for m in re.finditer(r"<script.*?</script>", s, re.S)}
    bad_amp = [i for i in raw_amp if not any(a <= i <= b for a, b in script)]
    if bad_amp:
        block(f"{len(bad_amp)} unescaped ampersand(s) outside <script>")

    # --- length advisories ------------------------------------------------
    for m in re.finditer(r'<article id="([^"]+)">(.*?)</article>', s, re.S):
        body = re.sub(r'<p class="sources">.*', "", m.group(2), flags=re.S)
        body = re.sub(r'<p class="corr">.*?</p>', "", body, flags=re.S)
        n = len(re.sub(r"<[^>]+>", " ", body).split())
        if n and not (240 <= n <= 430):
            warn(f"lead '{m.group(1)}' is {n} words (target ~250–400)")

    for sid, body in shorts:
        n = len(re.sub(r"<[^>]+>", " ", body).split())
        if not (130 <= n <= 280):
            warn(f"short '{sid}' is {n} words (target ~150–250)")

    # --- report -----------------------------------------------------------
    for w in WARN:
        print(f"  warn:  {w}")
    for b in BLOCK:
        print(f"  BLOCK: {b}")
    if BLOCK:
        print(f"\nFAILED — {len(BLOCK)} blocking issue(s). Do not publish.")
        return 1
    print("\nPASSED" + (f" with {len(WARN)} advisory warning(s)." if WARN else "."))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
