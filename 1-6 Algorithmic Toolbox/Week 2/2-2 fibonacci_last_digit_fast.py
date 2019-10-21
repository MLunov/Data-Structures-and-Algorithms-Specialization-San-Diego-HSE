# Uses python3

def fib_last_digit(n):
    if n <= 1:
        return n

    previous, current = 0, 1

    for i in range(n - 1):
        previous, current = current, (previous + current) % 10
    return current


print(fib_last_digit(int(input())))

# print(timeit.timeit("fib_last_digit(n = 327305)", setup="from __main__ import fib_last_digit", number=1))
# running time for fib_last_digit_bad(n = 327305) is 0.042244296


# def fib_last_digit_bad(n = 327305):
#     fib_seq = [0, 1]
#     for i in range(2, n + 1):
#         fib_seq.append((fib_seq[i - 1] + fib_seq[i - 2]) % 10)
#     return fib_seq[n]
#
#
# print(fib_last_digit_bad(int(input())))
#
# print(timeit.timeit("fib_last_digit_bad(n = 327305)", setup="from __main__ import fib_last_digit_bad", number=1))
# running time for fib_last_digit_bad(n = 327305) is 0.132780184
