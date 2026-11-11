#!/usr/bin/env python3
"""Parse an EIA weekly/monthly LeafHandler table into (year, 'MM/DD', value).

In the repo because this has been rewritten from scratch on several mornings
and has produced three silent failures in six weeks, each time by returning an
empty list rather than raising:

  28 Sep  matched class="B3" with double quotes; EIA serves class='B3'.
   8 Nov  the year cell is "&nbsp;&nbsp;2026-Oct", not a bare year.
  11 Nov  stock levels carry thousands separators ("105,138"), so float() threw
          on every row and the parser produced nothing.

Hence the assertion at the end: a parse that returns zero rows is a parser
failure, not a source failure. That rule has been in config.md since September;
now it raises.

Usage:  from tools.eia import parse_series   ->  [(2026, '10/30', 99259.0), ...]
        python3 -I tools/eia.py FILE.html [N]   prints the last N rows
"""
import html
import re
import sys

_YEAR = re.compile(r"<td class='B6'>(?:&nbsp;|\s)*(\d{4})")
_DATE = re.compile(r"<td class='B5'>(.*?)</td>")
_VAL = re.compile(r"<td class='B3'>(.*?)</td>")
_ROW = re.compile(r"(?is)<tr.*?</tr>")
_TAG = re.compile(r"<[^>]+>")


def _clean(cell):
    return html.unescape(_TAG.sub("", cell)).strip()


def parse_series(path, label=None):
    rows = []
    page = open(path, encoding="utf-8", errors="replace").read()
    for row in _ROW.findall(page):
        ym = _YEAR.search(row)
        if not ym:
            continue
        year = int(ym.group(1))
        for d, v in zip(_DATE.findall(row), _VAL.findall(row)):
            d, v = _clean(d), _clean(v).replace(",", "")
            if not d or not v:
                continue
            try:
                rows.append((year, d, float(v)))
            except ValueError:
                continue          # "W", "NA", "-" are genuine EIA no-data marks
    assert rows, (
        f"EIA parse returned ZERO rows for {label or path}. "
        "Assume the parser before the source: check the class quoting, the "
        "year cell's &nbsp; prefix, and thousands separators in the values."
    )
    return rows


def chronological(rows, year=None):
    """Sort by (year, month, day); optionally filter to one year."""
    if year is not None:
        rows = [r for r in rows if r[0] == year]
    return sorted(rows, key=lambda r: (r[0], int(r[1].split("/")[0]), int(r[1].split("/")[1])))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: eia.py FILE.html [N]")
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    for r in parse_series(sys.argv[1])[-n:]:
        print(r)
