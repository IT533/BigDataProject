#!/bin/sh
date
echo '--------------------------------------------------------------------------------'
python3 src/example.py input/allfile.txt > output/counts
echo '--------------------------------------------------------------------------------'
date