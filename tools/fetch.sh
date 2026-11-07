#!/bin/bash
# Logs every fetch to fetchlog.tsv: url, http code, bytes, local file.
# Exists because on 6 Nov two sources were downloaded, never parsed, and
# then reported in print as unreachable. The log is the evidence.
LOG="$(dirname "$0")/fetchlog.tsv"
u="$1"; o="$2"
r=$(curl -sS -L -m 35 -A 'news-brief/1.0' -o "$o" -w "%{http_code}\t%{size_download}" "$u" 2>/dev/null)
printf '%s\t%s\t%s\n' "$u" "$r" "$o" >> "$LOG"
printf '%s  %s\n' "$r" "$o"
