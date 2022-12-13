from rlist import random_list
n = int(input())
a = [str(i) for i in random_list(n)]
prob0 = a.count('0') / n * 100
prob1 = (100 - prob0)
print('Список: ', *a)
print(f"Вероятность выпадения 0: {prob0}%")
print(f"Вероятность выпадения 1: {prob1}%")

rows, r = [], a[0]

for i in range(n - 1):
    if a[i] == a[i + 1]:
        r += a[i + 1]
    else:
        if len(r) != 1:
            rows.append(r)
        r = a[i + 1]
if len(r) != 1:
    rows.append(r)

rows2, p, start = [], '', 0
for i in rows:
    c, start = 0, 0
    while c != len(i) and start != len(i) - 1:
        for j in range(start, len(i)):
            p += i[j]
            if len(i) > len(p) > 1:
                rows2.append(p)
        c += 1
        start += 1
        p = ''

rows += rows2
row_dict = {}

for i in sorted(set(rows), key=lambda x: len(x)):
    row_dict[i] = rows.count(i)

for i in row_dict:
     print(f"Вероятность последовательности {i}: {row_dict[i] / n * 100}%")