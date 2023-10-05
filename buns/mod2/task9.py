a = 'аеёиоуыэюя'
s = str(input())
gl = 0
co = 0
for i in s:
    if i in a:
        gl += 1
    elif i != " ":
        co += 1
print(gl, co)


