#!/bin/sh
cut -f1 -d $'\t' popular-names.txt | LANG=C sort | uniq -c | sort -r -k 2 -t ' '