# Uses python3

def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    return a


def lcm(a, b):
    return int(a / gcd(a, b)) * b


print(lcm(*map(int, input().split())))

# print(timeit.timeit("lcm(a = 761457, b = 614573)", setup="from __main__ import lcm", number=1))
# for lcm (a = 761457, b = 614573) runing time is 3.079000000000276e-05


# def lcm_bad(a, b):
#     mx, mn = max(a, b), min(a, b)
#     for i in range(1, mx):
#         if mx * i % mn == 0:
#             return (mx * i)
# 
# 
# print(lcm_bad(*map(int, input().split())))

# print(timeit.timeit("lcm_bad(a = 761457, b = 614573)", setup="from __main__ import lcm_bad", number=1))
# for lcm_bad (a = 761457, b = 614573) running time is 0.179243078
