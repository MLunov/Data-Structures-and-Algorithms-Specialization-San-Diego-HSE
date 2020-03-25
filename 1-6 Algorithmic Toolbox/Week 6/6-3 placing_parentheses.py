# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def MinAndMax(i, j):
    MIN = float('inf')
    MAX = float('-inf')

    for k in range(i, j):
        a = evalt(M[i][k], M[k + 1][j], op[k - 1])
        b = evalt(M[i][k], m[k + 1][j], op[k - 1])
        c = evalt(m[i][k], M[k + 1][j], op[k - 1])
        d = evalt(m[i][k], m[k + 1][j], op[k - 1])

        MIN = min(MIN, a, b, c, d)
        MAX = max(MAX, a, b, c, d)

    return (MIN, MAX)


dataset = list(input())

digits = [int(dataset[i]) for i in range(0, len(dataset), 2)]
op = [dataset[i] for i in range(1, len(dataset), 2)]

m, M, n = [], [], len(digits)
for i in range(n + 1):
    m.append([])
    M.append([])
    for j in range(n + 1):
        m[i].append(0)
        M[i].append(0)

for i in range(1, n + 1):
    m[i][i], M[i][i] = digits[i - 1], digits[i - 1]

for s in range(1, n):
    for i in range(1, n + 1 - s):
        j = i + s
        m[i][j], M[i][j] = MinAndMax(i, j)

# print(m)
# print(M)

print(M[1][n])
