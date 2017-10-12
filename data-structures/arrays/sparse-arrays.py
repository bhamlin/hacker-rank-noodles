#!/usr/bin/python3

import sys

data_count = int(input().strip())
data = list()
for _ in range(data_count):
    data.append(input().strip())

query_count = int(input().strip())
for query in map(str.strip, sys.stdin):
    print(len([x for x in data if x == query]))