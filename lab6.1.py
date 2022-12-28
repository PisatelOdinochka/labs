s = input('Введите скобочное выражение>>')
a = []
b = []
test = False
for i in range(len(s)):
    if s[i] == "(":
        a.append("(")
        b.append(s[i])
    else:
        if len(b) == 0:
            print(i, s[i])
            test = True
            break
        else:
            a.pop()
            b.pop()
if len(b) != 0 and not test:
     print("it's right!")