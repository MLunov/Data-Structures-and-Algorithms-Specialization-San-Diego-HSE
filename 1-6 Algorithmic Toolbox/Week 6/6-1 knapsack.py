# Uses python3
import sys


def optimal_weight(W, n, w):
    value = []
    for i in range(W + 1):
        value.append([])
        for j in range(n + 1):
            value[i].append(0)

    for j in range(1, n + 1):
        for i in range(1, W + 1):
            value[i][j] = value[i][j - 1]
            if w[j - 1] <= i:
                val = value[i - w[j - 1]][j - 1] + w[j - 1]
                if value[i][j] < val:
                    value[i][j] = val

    # print(value)

    return value[W][n]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, n, w))
