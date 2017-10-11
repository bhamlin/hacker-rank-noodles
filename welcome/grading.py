#!/bin/python3

import sys

from math import ceil

def round_grade(value):
   if value < 38:
      return value
   next_five = ceil(value / 5) * 5
   if (next_five - value) < 3:
      return next_five
   else:
      return value

input() # Each grade can be operated on individually
# A streaming approach will be used instead

for grade in map(lambda u: int(u.strip()), sys.stdin):
   print(round_grade(grade))
