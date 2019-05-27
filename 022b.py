n = int(input())
a = {}
for i in range(n):
    tmp = int(input())
    a[tmp] = a.get(tmp, 0) + 1
c = 0
for i in a.values():
    if i >= 2:
        c += i - 1
print(c)

