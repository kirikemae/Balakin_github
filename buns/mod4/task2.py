def i(a, n):
    if n % 2 == 0:
        return int((a ** 2) ** (n / 2))
    return int(a * a ** (n - 1))


print(i(*map(int, input().split())))
