#!/usr/bin/env bash
echo "Start"
scp ljc:/home/linaro/test_second* ./
python ./multi_fig.py
echo "End"


