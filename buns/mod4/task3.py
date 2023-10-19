def i(a, n):
    if n == 0:
        return a
    else:
        return i(n, a % n)


print(i(*map(int, input().split())))
