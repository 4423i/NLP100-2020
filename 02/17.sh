#!/bin/sh
cut -f1 -d$'\t' popular-names.txt | uniq | LANG=C sort