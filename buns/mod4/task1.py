a = list(str(input()))

l = len(set(a))

if l == 1:
    print("Все числа равны")
elif l == len(a):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")