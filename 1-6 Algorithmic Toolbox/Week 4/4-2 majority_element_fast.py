# Uses python3
import sys


def get_majority_element(a, n):
    countDict = {}
    for elem in a:
        countDict[elem] = countDict.get(elem, 0) + 1
    if max(countDict.values()) > n / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, n))

# def get_majority_element(a, left, right):
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     idx_mid = l + math.floor((r - l) / 2)
#     mid_value = a[idx_mid]
#     get_majority_element(a, left, idx_mid)
#     get_majority_element(a, idx_mid + 1, right)
#     return -1


# sorted_x = sorted(countDict.items(), key=lambda kv: -kv[1])
# maj_el = max([(value, key) for key, value in countDict.items()])
# if maj_el[0] > n / 2:
