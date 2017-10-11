#!/bin/python3

import sys

from functools import reduce
from operator import add

def birthdayCakeCandles(n, ar):
    max_candle = max(ar)
    return reduce(add, map(lambda v: int(v / max_candle), ar))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
