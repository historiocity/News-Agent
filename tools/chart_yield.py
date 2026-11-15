#!/usr/bin/env python3
"""Draw a year of the ten-year Treasury par yield as inline SVG, from the CSV.

In the repo because the chart code has been rewritten every morning it was
needed and produced a label collision on four of them (7, 11, 12, 13 November
2026). The rules those mornings cost are enforced here rather than remembered:

  * every geometric constant is derived, stated and asserted, and every plotted
    point is checked to be inside the box before anything is emitted;
  * label boxes are computed and tested pairwise, so a label collision raises
    instead of shipping. A label colliding with the DATA LINE is invisible to
    this check -- only a screenshot readback catches that, and the standing rule
    is to REMOVE such a label, never to nudge it twice.

Addressing a column: by HEADER, never by position. The 2026 file has fifteen
columns with the ten-year at index twelve; the 2023 and 2024 files have fourteen
with it at eleven, because the series gained a 1.5-month tenor in 2025. Counting
columns lands on the seven-year -- which is how the 18 September 2026 correction
came to retract a story that was true.

Usage:  python3 -I tools/chart_yield.py treasury.csv [COLUMN] > chart.svg
"""
import csv
import datetime
import sys

COL = sys.argv[2] if len(sys.argv) > 2 else "10 Yr"
rows = list(csv.reader(open(sys.argv[1])))
hdr = rows[0]
assert hdr.count(COL) == 1, (COL, hdr)          # by header, never by position
i = hdr.index(COL)


def _d(r):
    return datetime.datetime.strptime(r[0], "%m/%d/%Y").date()


pts = sorted([(_d(r), float(r[i])) for r in rows[1:] if r[i]], key=lambda x: x[0])
n = len(pts)
assert n >= 100, f"only {n} sessions parsed from {sys.argv[1]} -- suspect the parser"

# geometry: derived, then asserted
X0, X1 = 46.0, 686.0            # plot box inside a 700-wide viewBox
Y0, Y1 = 20.0, 232.0
lo, hi = min(v for _, v in pts), max(v for _, v in pts)
VMIN = (lo * 10 // 1) / 10 - 0.0 if False else round(lo - 0.07, 1)
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
cross = next((k for k, (_, v) in enumerate(pts) if v >= 5.00), None)

out = []
A = out.append
A('<svg viewBox="0 0 700 272" role="img" aria-label="%s Treasury par yield by '
  'session, with the 5 percent line">' % COL)
A("<title>%s Treasury par yield</title>" % COL)
import math
grid = []
g = math.ceil(VMIN / 0.25) * 0.25          # first round quarter-point above the floor
while g < VMAX - 1e-9:
    if g > VMIN + 1e-9:
        grid.append(round(g, 2))
    g += 0.25
for v in grid:
    yy, em = y(v), abs(v - 5.00) < 1e-9
    A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"%s/>' % (
        X0, yy, X1, yy, "currentColor" if em else "#9aa0a6",
        "1.1" if em else "0.5", ' stroke-dasharray="5 4"' if em else ' opacity="0.45"'))
    A('<text x="%.1f" y="%.1f" font-size="10" fill="currentColor" opacity="%s" '
      'text-anchor="end">%.2f</text>' % (X0 - 5, yy + 3, "0.95" if em else "0.6", v))
A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="currentColor" '
  'stroke-width="0.8" opacity="0.6"/>' % (X0, Y1, X1, Y1))
seen = set()
for k, (dt, _) in enumerate(pts):
    if dt.month in seen:
        continue
    seen.add(dt.month)
    A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="currentColor" '
      'stroke-width="0.6" opacity="0.5"/>' % (x(k), Y1, x(k), Y1 + 4))
    A('<text x="%.1f" y="%.1f" font-size="10" fill="currentColor" opacity="0.6" '
      'text-anchor="middle">%s</text>' % (x(k), Y1 + 16, dt.strftime("%b")))
A('<path d="%s" fill="none" stroke="currentColor" stroke-width="1.5"/>' % path)

FS = 10.5
CHW = FS * 0.55                 # mean glyph width at this size, used for the box test
labels = []
if cross is not None:
    labels.append((cross, pts[cross][1],
                   "%d %s · %.2f" % (pts[cross][0].day,
                                          pts[cross][0].strftime("%b"), pts[cross][1]),
                   -6.5, "end"))
labels.append((kmax, pts[kmax][1],
               "%d %s · %.2f high" % (pts[kmax][0].day,
                                           pts[kmax][0].strftime("%b"), pts[kmax][1]),
               -10, "middle"))
boxes = []
for k, v, lab, dy, anc in labels:
    tx = x(k) + (0 if anc == "middle" else -6)
    w = len(lab) * CHW
    x0 = tx - (w / 2 if anc == "middle" else w)
    ty = y(v) + dy
    boxes.append((x0, x0 + w, ty - FS, ty + 2, lab))
for a in range(len(boxes)):
    assert 0 <= boxes[a][0] and boxes[a][1] <= 700, "label off canvas: %r" % boxes[a][4]
    for b in range(a + 1, len(boxes)):
        A0, A1_, At, Ab, la = boxes[a]
        B0, B1_, Bt, Bb, lb = boxes[b]
        assert not (A0 < B1_ and B0 < A1_ and At < Bb and Bt < Ab), \
            "label collision: %r vs %r -- REMOVE one, do not nudge" % (la, lb)
for (k, v, lab, dy, anc) in labels:
    A('<circle cx="%.1f" cy="%.1f" r="3.1" fill="currentColor"/>' % (x(k), y(v)))
    A('<text x="%.1f" y="%.1f" font-size="%s" fill="currentColor" text-anchor="%s">%s</text>'
      % (x(k) + (0 if anc == "middle" else -6), y(v) + dy, FS, anc,
         lab.replace("·", "&#183;")))
A('<circle cx="%.1f" cy="%.1f" r="3.1" fill="currentColor"/>' % (x(n - 1), y(pts[-1][1])))
A('<text x="%.1f" y="%.1f" font-size="10" fill="currentColor" opacity="0.6">per cent</text>'
  % (X0 - 4, 12))
A("</svg>")
print("\n".join(out))
sys.stderr.write("OK n=%d range %.2f-%.2f pxpy=%.4f pxpx=%.4f last=%s\n"
                 % (n, VMIN, VMAX, PXPY, PXPX, pts[-1]))
