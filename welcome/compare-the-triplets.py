#!/usr/bin/python3

import sys
from functools import reduce
from operator import add

def trip_comp(p):
    u, v = p
    if u > v:
        return (1, 0)
    elif u < v:
        return (0, 1)
    else:
        return (0, 0)

def trip_reduce(u, v):
    return tuple(map(lambda values: add(*values), zip(u, v)))

def solve(values):
    return reduce(trip_reduce, map(trip_comp, zip(*values)))

inputs = list()

for line in map(str.strip, sys.stdin):
    inputs.append(tuple(map(int, line.split(' '))))

if len(inputs) > 2:
    sys.exit('Currently only supports two data sets. You provided {}.'
            .format(len(inputs)))

result = solve(inputs)
print(" ".join(map(str, result)))
