def i(s):
    d = {x: s.count(x) for x in set(s)}
    if sum(x % 2 for x in d.values()) <= 1:
        st = ''
        for j, k in d.items():
            st += j * (k // 2)
            if k % 2 != 0:
                mid = j
        print(st + mid + st[::-1])


i(input())
