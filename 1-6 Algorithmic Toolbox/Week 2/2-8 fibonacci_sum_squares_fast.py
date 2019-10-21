# Uses python3

def fib_last_digit_sum_sq(n, m=10, pi=60):
    previous, current, sum = 0, 1, 1
    n = int(n % pi)

    if n <= 1:
        return n

    for i in range(n - 1):
        previous, current = current, (previous + current)
        sum = (sum + (current ** 2) % m) % m

    return sum


print(fib_last_digit_sum_sq(int(input())))

# import timeit
#
# print(timeit.timeit("fib_last_digit_sum_sq(n=1234567890, m=10, pi=60)",
#                     setup="from __main__ import fib_last_digit_sum_sq", number=1))
# # running time for fib_last_digit_sum_sq(n=1234567890, m=10, pi=60) is 4.2450999999998906e-05
