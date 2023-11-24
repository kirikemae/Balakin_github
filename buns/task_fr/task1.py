import re
pattern_gpt = re.compile(r'^(?=(?:.*[a-z]){2})(?=.*\d)(?=(?:.*[@$%^#&*]){3})(?!.*[,.!?])(?=.*[A-Za-z0-9@$%^#&*]).{8,}$')

print(bool(pattern_gpt.match("rtG&3FG#Tr^e")))
print(bool(pattern_gpt.match("a^A1@*@1Aa")))
print(bool(pattern_gpt.match("oF^a1D@y5%e6")))
print(bool(pattern_gpt.match("enroi#$*rkdeR#$*092uwedchf34tguv394h")))
print(bool(pattern_gpt.match("пароль")))
print(bool(pattern_gpt.match("password")))
print(bool(pattern_gpt.match("qwerty")))
print(bool(pattern_gpt.match("lOngPa$$W0Rd")))
