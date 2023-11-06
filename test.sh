#!/usr/bin/env bash
echo "Start"
scp ljc:/home/linaro/test* ./
python ./multi_compare.py
echo "End"


