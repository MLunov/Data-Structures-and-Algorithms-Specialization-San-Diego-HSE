# Uses python3
import sys


def mergeSort(myList, inv):
    n = len(myList)
    if n == 1:
        return myList, inv
    a = mergeSort(myList[:int(n / 2)], inv)
    b = mergeSort(myList[int(n / 2):], inv)
    i, j, c, inv = 0, 0, [], a[1] + b[1]
    for k in range(n):
        if a[0][i] <= b[0][j]:
            c.append(a[0][i])
            i += 1
            if i == int(len(a[0])):
                c.extend(b[0][j:])
                return c, inv
        else:
            c.append(b[0][j])
            j += 1
            inv += int(n / 2) - i
            if j == int(len(b[0])):
                c.extend(a[0][i:])
                return c, inv


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    # print(get_number_of_inversions(a, b, 0, len(a)))
    answer = mergeSort(a, 0)
    print(answer[1])

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     #write your code here
#     return number_of_inversions
