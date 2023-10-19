st = open(input(), 'r', encoding='utf-8').read()
with open('output.txt', 'w', encoding='utf-8') as file:
    for i, j in dict(sorted({x: st.count(x) for x in set(st) if x.isalpha()}.items(), key=lambda i: i[1])).items():
        file.write(str(i) + " : " + str(j) + '\n')
