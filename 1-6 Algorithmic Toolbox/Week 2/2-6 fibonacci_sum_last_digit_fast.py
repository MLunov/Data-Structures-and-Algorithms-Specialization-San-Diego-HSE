# Uses python3
# import timeit


# def pisanoPeriod_sum(m):
#     previous, current, sum = 0, 1, 1
#
#     for i in range(0, m * m):
#         previous, current = current, (previous + current) % m
#         sum = (sum + current) % m
#
#         # A Pisano Period starts with 01
#         if (previous == 0 and current == 1):
#             return i + 1, sum - current


def fib_last_digit_sum(n, m):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for i in range(n - 1):
        previous, current = current, (previous + current) % m
        sum = (sum + current) % m
    return sum


def fib_sum(n, m=10):
    if n <= 1:
        return n

    pi = 60
    ## for m = 10 pi = 60 and pisanoPeriod_sum(m) % 10 = 0 (e.g. 280 % 10 = 0 !!!), \
    ## that's why we don't need to use this function in this case
    # pi, pi_sum = pisanoPeriod_sum(m)
    # return ((n // pi) * pi_sum + fib_last_digit_sum(int(n % pi), m)) % m

    return fib_last_digit_sum(int(n % pi), m)


print(fib_sum(int(input())))

# print(timeit.timeit("fib_sum(n=100, m=10)", setup="from __main__ import fib_sum", number=1))
# running time for fib_sum(n=100, m=10) is 2.3791999999994706e-05
