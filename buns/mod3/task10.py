a = int(input())
for i in range(a):
    print(", ".join([str(x) for x in range(1, a + 1)]))
print()
for i in range(a):
    print(", ".join([str(i + 1) for _ in range(a)]))
