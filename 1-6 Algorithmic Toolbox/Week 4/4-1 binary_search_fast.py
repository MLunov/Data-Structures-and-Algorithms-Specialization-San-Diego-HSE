# python3
# import time
# start_time = time.time()

import sys
import math


def binary_search(a, l, r, key):
    while l < r:
        idx_mid = l + math.floor((r - l) / 2)
        mid_value = a[idx_mid]
        if mid_value == key:
            return idx_mid
        elif key < mid_value:
            r = idx_mid
        else:
            l = idx_mid + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    # with open('sample.txt') as f:
    #     data = list(map(int, f.read().split()))
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        print(binary_search(a, 0, len(a), x), end=' ')

# print("--- %s seconds ---" % (time.time() - start_time))

# def binary_search(a, l, r, key):
#     idx_mid = l + math.ceil((r - l) / 2) - 1
#     mid_value = a[idx_mid]
#     if idx_mid + 1 == r:
#         if mid_value == key:
#             return idx_mid
#         else:
#             return -1
#     else:
#         if mid_value == key:
#             return idx_mid
#         elif key < mid_value:
#             return binary_search(a, l, idx_mid, key)
#         else:
#             return binary_search(a, idx_mid + 1, r, key)
