a = 0
for i in range(3):
    s, e = list(map(int, input().split(" ")))
    a += s * e * 0.1
print(int(a))