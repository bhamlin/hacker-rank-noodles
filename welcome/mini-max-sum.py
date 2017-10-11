#!/bin/python3

import sys

from functools import reduce
from itertools import combinations
from operator import add

arr = list(map(int, input().strip().split(' ')))

set_min, set_max = None, None

for combo in combinations(arr, 4):
    total = reduce(add, combo)
    if not set_min:
        set_min = total
    if not set_max:
        set_max = total
    
    set_min = min(total, set_min)
    set_max = max(total, set_max)

print(set_min, set_max)