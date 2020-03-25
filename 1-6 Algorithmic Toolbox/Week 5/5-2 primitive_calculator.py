# Uses python3
import sys


def optimal_sequence(n):
    minNumOp = [-1] * (n + 1)
    sequenceDict = {}

    for i in range(1, n + 1):
        minNumOp[i] = float('inf')
        sequenceDict.setdefault(i, [])

        for j in range(1, 4):

            if j == 1:
                Num = minNumOp[i - j] + 1
                if Num < minNumOp[i]:
                    minNumOp[i] = Num
                    sequenceDict[i].append(i - j)

            elif i % j == 0:
                Num = minNumOp[i // j] + 1
                if Num < minNumOp[i]:
                    minNumOp[i] = Num
                    sequenceDict[i].append(i // j)

    sequence = []
    while n != 0:
        sequence.append(n)
        n = sequenceDict[n][-1]

    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

# import sys
#
#
# def best_n2(n1):
#     if n1 % 3 == 0:
#         n2 = n1 // 3
#     elif n1 % 2 == 0:
#         n2 = n1 // 2
#     else:
#         n2 = n1 - 1
#     return n2
#
#
# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#
#         sequence.append(n)
#         min_n2 = float('inf')
#
#         for i in range(1, 4):
#
#             if i == 1:
#                 n1 = n - 1
#                 n2 = best_n2(n1)
#                 if n2 < min_n2:
#                     min_n2 = n2
#                     best_n1 = n1
#             else:
#                 if n % i == 0:
#                     n1 = n // i
#                     n2 = best_n2(n1)
#                     if n2 < min_n2:
#                         min_n2 = n2
#                         best_n1 = n1
#
#         n = best_n1
#
#     return reversed(sequence)
#
#
# input = sys.stdin.read()
# n = int(input)
# sequence = list(optimal_sequence(n))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')
