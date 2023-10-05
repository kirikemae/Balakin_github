a = str(input())
s = 0
p = 0
for i in a:
    if (a.index(i) + 1) % 2 == 0:
        s += int(i)
    else:
        p += int(i)
if (3*s + p) % 10 == 0:
    print('yes')
else:
    print('no')