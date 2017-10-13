from itertools import accumulate

n, m = map(int, input().split(' '))
dx = [0] * (n + 1) # allow run past end

for _ in range(m):
    a, b, c = map(int, input().split(' '))
    dx[a - 1] += c
    dx[b] -= c

print(max(accumulate(dx)))
