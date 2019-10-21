# python3
n, max_prod = int(input()), 0
numbers = list(map(int, input().split()))
for i in range(n - 1):
    for j in range(i + 1, n):
        max_prod = max(max_prod, numbers[i] * numbers[j])
print(max_prod)
