# Uses python3
import sys


def mergeSort(myList, w):
    n = len(myList)
    if n == 1:
        return myList, w
    a = mergeSort(myList[:int(n / 2)], w[:int(n / 2)])
    b = mergeSort(myList[int(n / 2):], w[int(n / 2):])
    i, j, c, d = 0, 0, [], []
    for k in range(n):
        if a[0][i] >= b[0][j]:
            c.append(a[0][i])
            d.append(a[1][i])
            i += 1
            if i == int(len(a[0])):
                c.extend(b[0][j:])
                d.extend(b[1][j:])
                return c, d
        else:
            c.append(b[0][j])
            d.append(b[1][j])
            j += 1
            if j == int(len(b[0])):
                c.extend(a[0][i:])
                d.extend(a[1][i:])
                return c, d


def get_optimal_value(capacity, weights, values):
    value, c = 0, 0
    u_val = []
    for i in range(n):
        u_val.append(values[i] / weights[i])
    u_val = mergeSort(u_val, weights)
    while capacity != 0 and c != n:
        a = min(capacity, u_val[1][c])
        value += a * u_val[0][c]
        capacity -= a
        c += 1
    return value


data = list(map(int, sys.stdin.read().split()))
n, capacity = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2 * n + 2):2]
opt_value = get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value))
