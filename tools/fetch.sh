#!/bin/bash
# Fetch a URL and log it. Every request this brief makes goes through here, so
# "could not reach" in the footer is checkable against a file instead of memory.
#
# Log: $FETCHLOG, else ./fetchlog.tsv in the CURRENT directory -- never beside
# this script, which on 8 Nov put the log inside the repository.
# Columns: url, http_code, bytes, local file.
set -u
LOG="${FETCHLOG:-$PWD/fetchlog.tsv}"
u="$1"; o="$2"
r=$(curl -sS -L -m 35 -A 'news-brief/1.0' -o "$o" -w '%{http_code}\t%{size_download}' "$u" 2>/dev/null)
printf '%s\t%s\t%s\n' "$u" "$r" "$o" >> "$LOG"
printf '%s  %s\n' "$r" "$o"
