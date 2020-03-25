# Uses python3
import sys


def get_change(m):
    minNumCoins = [0] * (m + 1)
    for i in range(1, m + 1):
        minNumCoins[i] = float('inf')
        for j in [1, 3, 4]:
            if i >= j:
                NumCoins = minNumCoins[i - j] + 1
                if NumCoins < minNumCoins[i]:
                    minNumCoins[i] = NumCoins

    return minNumCoins[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
