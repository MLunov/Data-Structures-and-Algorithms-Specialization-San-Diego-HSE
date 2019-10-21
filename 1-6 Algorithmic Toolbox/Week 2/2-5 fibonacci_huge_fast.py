# Uses python3

def pisanoPeriod(m):
    previous, current = 0, 1

    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


def fib_last_digit(n, m):
    if n <= 1:
        return n

    previous, current = 0, 1

    for i in range(n - 1):
        previous, current = current, (previous + current) % m
    return current


def fib_huge(n, m):
    pi = pisanoPeriod(m)
    return fib_last_digit(int(n % pi), m)


print(fib_huge(*map(int, input().split())))

# print(timeit.timeit("fib_huge(n = 2816213588, m = 239)", setup="from __main__ import fib_huge", number=1))
# running time for fib_huge(n = 239, m = 1000) is 0.00043058399999999775
# running time for fib_huge(n = 2816213588, m = 239) is 6.531100000000192e-05
