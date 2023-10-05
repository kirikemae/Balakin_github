from string import ascii_lowercase
a = str(input())
b = int(input())
i = ascii_lowercase.index(a) + b
print(ascii_lowercase[i%len(ascii_lowercase)])