# python3
import sys


def compute_min_refills(tank, n, stops):
    numR, curR = 0, 0
    while curR < n:
        lastR = curR
        while (curR < n) and (stops[curR + 1] - stops[lastR] <= tank):
            curR += 1
        if curR == lastR:
            return -1
        if curR < n:
            numR += 1
    return numR


if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(m, n + 1, [0] + stops + [d]))
