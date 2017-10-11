#!/bin/python3

import sys


def get_value(arr, coord):
    x, y = coord
    return arr[y][x]

def get_offset_value(arr, coord, coord_offset):
    return get_value(arr, tuple(map(sum, zip(coord, coord_offset))))

def get_hourglass(arr, indices, coord):
    return list(map(lambda q: get_offset_value(arr, coord, q), indices))

if __name__ == '__main__':
    arr = []
    for arr_i in map(str.strip, sys.stdin):
       arr_t = [int(n) for n in arr_i.split(' ')]
       arr.append(arr_t)
    
    H_OFFSET_X = 2
    H_OFFSET_Y = 2
    H_INDICES = ((0, 0), (1, 0), (2, 0), (1, 1), (0, 2), (1, 2), (2, 2))

    MAX_X = max(map(len, arr)) - H_OFFSET_X
    MAX_Y = len(arr) - H_OFFSET_Y
    
    highest_total = -100
    
    for x in range(MAX_X):
        for y in range(MAX_Y):
            total = sum(get_hourglass(arr, H_INDICES, (x, y)))
            print(total)
            highest_total = max(highest_total, total)
            
print(highest_total)