# Uses python3

def fib_last_digit_sum(n, m):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for i in range(n - 1):
        previous, current = current, (previous + current) % m
        sum = (sum + current) % m

    return sum


def fib_part_sum(n, k, m=10, pi=60):
    # for m = 10 pi = 60 and pisanoPeriod_sum(m) % 10 = 0 (e.g. 280 % 10 = 0 !!!)
    return (m + fib_last_digit_sum(int(k % pi), m) - fib_last_digit_sum(int((n - 1) % pi), m)) % m


print(fib_part_sum(*map(int, input().split())))

# import timeit
#
#
# print(timeit.timeit("fib_part_sum(n=10, k=200, m=10, pi=60)", setup="from __main__ import fib_part_sum", number=1))
# # running time for fib_part_sum(n=10, k=200) is 1.9127000000000727e-05


# def fib_part_sum_wrong(n, k, m=10, pi=60):
#     sum, current, next = 0, 0, 1
#     from_, to = int(n % pi), int(k % pi)
#     print(from_, to)
#
#     for i in range(to + 1):
#         if i >= from_:
#             sum = (sum + current) % m
#
#         current, next = next, (current + next) % m
#
#     return sum
#
#
# print(fib_part_sum_wrong(*map(int, input().split())))
#
# # import timeit
# #
# #
# # print(timeit.timeit("fib_part_sum_wrong(n=10, k=200)", setup="from __main__ import fib_part_sum_wrong", number=1))
# # # running time for fib_part_sum_wrong(n=10, k=200) is 1.4927999999997388e-05
