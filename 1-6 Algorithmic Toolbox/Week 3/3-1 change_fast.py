# Uses python3

def get_change(m):
    return m // 10 + (m % 10) // 5 + ((m % 10) % 5)


print(get_change(int(input())))
