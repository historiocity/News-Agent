#!/usr/bin/env python3
"""Extract text from a Federal Register / GovInfo PDF without external deps.

Lives in the repo rather than a session scratchpad because the scratchpad dies
with the container and this gets rewritten from scratch every time it does --
the same mistake that kept the issue validator unversioned until 4 November.

Usage: python3 -I tools/pdftext.py FILE.pdf [> out.txt]
"""
import re, sys, zlib

OCTAL = {
    b"\\221": b"'", b"\\222": b"'", b"\\223": b'"', b"\\224": b'"',
    b"\\226": b"-", b"\\227": b"--", b"\\205": b"...", b"\\267": b"*",
}

def streams(data):
    for m in re.finditer(rb"stream\r?\n(.*?)endstream", data, re.S):
        raw = m.group(1)
        try:
            yield zlib.decompress(raw)
        except zlib.error:
            try:
                yield zlib.decompressobj().decompress(raw)
            except zlib.error:
                continue

def text_of(chunk):
    out = []
    # Tj / TJ string operands
    for m in re.finditer(rb"\((?:\\.|[^()\\])*\)", chunk):
        s = m.group(0)[1:-1]
        for k, v in OCTAL.items():
            s = s.replace(k, v)
        s = re.sub(rb"\\([()\\])", rb"\1", s)
        s = re.sub(rb"\\[0-7]{1,3}", b"", s)
        out.append(s)
    return b"".join(out)

def main(path):
    data = open(path, "rb").read()
    pages = []
    for chunk in streams(data):
        t = text_of(chunk)
        if t.strip():
            pages.append(t.decode("latin-1", "replace"))
    sys.stdout.write("\n\n=== PAGE ===\n\n".join(pages))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: pdftext.py FILE.pdf")
    main(sys.argv[1])
