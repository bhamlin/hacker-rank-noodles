#!/usr/bin/python3

import sys

N, _ = map(int, input().strip().split(' '))

seq = [0] * N

for line in map(str.strip, sys.stdin):
    a, b, k = map(int, line.split(' '))
    for i in range(a-1, b):
        seq[i] += k

print(max(seq))
# crush.2 2490686975
