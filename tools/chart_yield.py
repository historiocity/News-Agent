#!/usr/bin/env python3
"""Draw a Treasury par-yield series as inline SVG, straight from Treasury's CSVs.

In the repo because the chart code was rewritten every morning it was needed and
produced a label collision on four of them (7, 11, 12, 13 November 2026). The
rules those mornings cost are enforced here rather than remembered:

  * every geometric constant is derived, stated and asserted, and every plotted
    point is checked to be inside the box before anything is emitted;
  * label boxes are computed and tested pairwise, so a label collision raises
    instead of shipping. A label colliding with the DATA LINE is invisible to
    this check -- only a screenshot readback catches that, and the standing rule
    is to REMOVE such a label, never to nudge it twice.

Addressing a column: by HEADER, never by position, and re-read PER FILE, because
the position moves. Treasury's 2007-2021 files have twelve columns with the
ten-year at index nine; 2022-2024 have fourteen with it at eleven; 2025-2026
have fifteen with it at twelve, the series having gained a 1.5-month tenor in
2025. Counting columns lands on the seven-year -- which is how this brief's
18 September 2026 correction came to retract a story that was true.

Usage:  python3 -I tools/chart_yield.py FILE.csv [FILE.csv ...] \
            [--col "10 Yr"] [--mark YYYY-MM-DD] ... > chart.svg

Several CSVs concatenate into one series, so a multi-year chart is just the year
files listed together. --mark labels a named session; with none given, the first
session at or above 5.00% is labelled. The series maximum is always labelled.
"""
import csv
import datetime
import math
import sys

args = sys.argv[1:]
COL, marks, files = "10 Yr", [], []
while args:
    a = args.pop(0)
    if a == "--col":
        COL = args.pop(0)
    elif a == "--mark":
        marks.append(datetime.date.fromisoformat(args.pop(0)))
    else:
        files.append(a)
assert files, "no CSV given; see the module docstring"


def _d(r):
    return datetime.datetime.strptime(r[0], "%m/%d/%Y").date()


pts = []
for f in files:
    rows = list(csv.reader(open(f)))
    hdr = rows[0]
    assert hdr.count(COL) == 1, (f, COL, hdr)   # by header, never by position
    i = hdr.index(COL)                          # recomputed per file: it moves
    got = [(_d(r), float(r[i])) for r in rows[1:] if len(r) > i and r[i]]
    assert got, f"no rows parsed from {f} -- suspect the parser, not the source"
    pts += got
pts.sort(key=lambda x: x[0])
assert len({d for d, _ in pts}) == len(pts), "the files overlap: duplicate sessions"
n = len(pts)
assert n >= 100, f"only {n} sessions parsed -- suspect the parser"

# geometry: derived, then asserted
X0, X1 = 46.0, 686.0            # plot box inside a 700-wide viewBox
Y0, Y1 = 20.0, 232.0
lo = min(v for _, v in pts)
hi = max(v for _, v in pts)
VMIN = round(lo - 0.07, 1)
VMAX = round(hi + 0.09, 1)
PXPY = (Y1 - Y0) / (VMAX - VMIN)   # px per percentage point
PXPX = (X1 - X0) / (n - 1)         # px per session


def x(k):
    return X0 + k * PXPX


def y(v):
    return Y1 - (v - VMIN) * PXPY


assert x(0) == X0 and abs(x(n - 1) - X1) < 1e-9
assert abs(y(VMIN) - Y1) < 1e-9 and abs(y(VMAX) - Y0) < 1e-9
assert max(x(k) for k in range(n)) <= 700, "max x outside the viewBox"
for dt, v in pts:
    assert VMIN <= v <= VMAX and Y0 <= y(v) <= Y1, (dt, v)

path = " ".join(("M" if k == 0 else "L") + "%.1f %.1f" % (x(k), y(v))
                for k, (_, v) in enumerate(pts))

kmax = max(range(n), key=lambda k: pts[k][1])
index = {d: k for k, (d, _) in enumerate(pts)}
if marks:
    picks = []
    for m in marks:
        assert m in index, f"--mark {m} is not a session in these files"
        picks.append(index[m])
else:
    c = next((k for k, (_, v) in enumerate(pts) if v >= 5.00), None)
    picks = [c] if c is not None else []

SPAN = pts[-1][0].year - pts[0][0].year
TICK = "%Y" if SPAN >= 3 else "%b"

out = []
A = out.append
A('<svg viewBox="0 0 700 272" role="img" aria-label="%s Treasury par yield by '
  'session, with the 5 per cent line">' % COL)
A("<title>%s Treasury par yield</title>" % COL)
step = 0.5 if (VMAX - VMIN) > 3 else 0.25
g = math.ceil(VMIN / step) * step
while g < VMAX - 1e-9:
    if g > VMIN + 1e-9:
        yy, em = y(g), abs(g - 5.00) < 1e-9
        A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
          'stroke-width="%s"%s/>' % (X0, yy, X1, yy, "currentColor" if em else "#9aa0a6",
                                     "1.1" if em else "0.5",
                                     ' stroke-dasharray="5 4"' if em else ' opacity="0.45"'))
        A('<text x="%.1f" y="%.1f" font-size="10" fill="currentColor" opacity="%s" '
          'text-anchor="end">%.2f</text>' % (X0 - 5, yy + 3, "0.95" if em else "0.6", g))
    g += step
A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="currentColor" '
  'stroke-width="0.8" opacity="0.6"/>' % (X0, Y1, X1, Y1))
seen, every = set(), max(1, (SPAN + 1) // 11)
for k, (dt, _) in enumerate(pts):
    key = dt.year if SPAN >= 3 else dt.month
    if key in seen:
        continue
    seen.add(key)
    if SPAN >= 3 and (dt.year % every):
        continue
    A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="currentColor" '
      'stroke-width="0.6" opacity="0.5"/>' % (x(k), Y1, x(k), Y1 + 4))
    A('<text x="%.1f" y="%.1f" font-size="10" fill="currentColor" opacity="0.6" '
      'text-anchor="middle">%s</text>' % (x(k), Y1 + 16, dt.strftime(TICK)))
A('<path d="%s" fill="none" stroke="currentColor" stroke-width="1.5"/>' % path)

FS = 10.5
CHW = FS * 0.55                 # mean glyph width at this size, used for the box test
DOT = "&#183;"


def _lab(k, suffix=""):
    d, v = pts[k]
    when = d.strftime("%b %Y") if SPAN >= 3 else "%d %s" % (d.day, d.strftime("%b"))
    return "%s %s %.2f%s" % (when, DOT, v, suffix)


def _anchor(k):
    return "end" if x(k) > 600 else ("start" if x(k) < 120 else "middle")


labels = [(k, pts[k][1], _lab(k), -6.5, _anchor(k)) for k in picks if k != kmax]
labels.append((kmax, pts[kmax][1], _lab(kmax, " high"), -10, _anchor(kmax)))

boxes = []
for k, v, lab, dy, anc in labels:
    off = 0 if anc == "middle" else (6 if anc == "start" else -6)
    w = len(lab.replace(DOT, ".")) * CHW
    tx = x(k) + off
    x0 = tx - (w / 2 if anc == "middle" else (0 if anc == "start" else w))
    ty = y(v) + dy
    boxes.append((x0, x0 + w, ty - FS, ty + 2, lab))
for a in range(len(boxes)):
    assert 0 <= boxes[a][0] and boxes[a][1] <= 700, "label off canvas: %r" % boxes[a][4]
    for b in range(a + 1, len(boxes)):
        A0, A1_, At, Ab, la = boxes[a]
        B0, B1_, Bt, Bb, lb = boxes[b]
        assert not (A0 < B1_ and B0 < A1_ and At < Bb and Bt < Ab), \
            "label collision: %r vs %r -- REMOVE one, do not nudge" % (la, lb)
for k, v, lab, dy, anc in labels:
    off = 0 if anc == "middle" else (6 if anc == "start" else -6)
    A('<circle cx="%.1f" cy="%.1f" r="3.1" fill="currentColor"/>' % (x(k), y(v)))
    A('<text x="%.1f" y="%.1f" font-size="%s" fill="currentColor" text-anchor="%s">%s</text>'
      % (x(k) + off, y(v) + dy, FS, anc, lab))
A('<circle cx="%.1f" cy="%.1f" r="3.1" fill="currentColor"/>' % (x(n - 1), y(pts[-1][1])))
A('<text x="%.1f" y="%.1f" font-size="10" fill="currentColor" opacity="0.6">per cent</text>'
  % (X0 - 4, 12))
A("</svg>")
print("\n".join(out))
sys.stderr.write("OK n=%d range %.2f-%.2f pxpy=%.4f pxpx=%.5f first=%s last=%s\n"
                 % (n, VMIN, VMAX, PXPY, PXPX, pts[0], pts[-1]))
