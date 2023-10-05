a = list()
for i in range(0, 3):
    ele = int(input())
    if ele > 1000 or ele < -1000:
        print('Ошибка')
        exit()
    a.append(ele)
sorted(a)
print(a[1])
