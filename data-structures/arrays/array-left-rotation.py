#!/bin/python3

import sys

# # Never mind, Python doesn't tail recurse
# def leftRotation(a, d):
#     if d <= 0:
#         return a
#     else:
#         return leftRotation(a[1:] + [a[0]], d - 1)
def leftRotation(a, d):
    return a[d:] + a[:d]

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    d = d % n
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))
