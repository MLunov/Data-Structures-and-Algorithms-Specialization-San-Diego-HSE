# python3

n = int(input())
numbers = list(map(int, input().split()))
n1 = max(numbers)
numbers.remove(n1)
print(n1 * max(numbers))

# n = int(input())
# numbers = sorted(list(map(int, input().split())))
# print(numbers[-1] * numbers[-2])

# n, ind1 = int(input()), 0
# numbers = list(map(int, input().split()))
# for i in range(1, n):
#     if numbers[i] > numbers[ind1]:
#         ind1 = i
# if ind1 == 0:
#     ind2 = 1
# else:
#     ind2 = 0
# for i in range(1, n):
#     if i != ind1 and numbers[i] > numbers[ind2]:
#         ind2 = i
# print(numbers[ind1] * numbers[ind2])
