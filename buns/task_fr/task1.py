import re
pattern_pass = re.compile(r'^(?=(?:.*[a-z]){2})(?=.*\d)(?=(?:.*[@$%^#&*]){3})(?!.*[,.!?])(?=.*[A-Za-z0-9@$%^#&*]).{8,}$')

print(bool(pattern_pass.match("rtG&3FG#Tr^e")))
print(bool(pattern_pass.match("a^A1@*@1Aa")))
print(bool(ppattern_pass.match("oF^a1D@y5%e6")))
print(bool(pattern_pass.match("enroi#$*rkdeR#$*092uwedchf34tguv394h")))
print(bool(pattern_pass.match("пароль")))
print(bool(pattern_pass.match("password")))
print(bool(pattern_pass.match("qwerty")))
print(bool(pattern_pass.match("lOngPa$$W0Rd")))
