#!/usr/bin/python3

import sys

def tuple_gen(N):
    l = list()
    for _ in range(N):
        l.append(list())
    return tuple(l)

def func_gen(seq, N):
    index = lambda x, last_answer: (x ^ last_answer) % N
    def f(last_answer, x=0, y=0):
        seq[index(x, last_answer)].append(y)
        return last_answer
    def g(last_answer, x=0, y=0):
        L = seq[index(x, last_answer)]
        V = L[y % len(L)]
        return V
    
    return (f, g)

N, Q = map(int, input().strip().split(' '))

seq = tuple_gen(N)

funcs = func_gen(seq, N)

last_answer = 0
for line in map(str.strip, sys.stdin):
    f, x, y = map(int, line.split(' '))
    last_answer = funcs[f - 1](last_answer, x, y)
    if f == 2:
        print(last_answer)
