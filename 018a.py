a = int(input())
b = int(input())
c = int(input())
d = sorted([a, b, c], reverse=True)
print(d.index(a) + 1)
print(d.index(b) + 1)
print(d.index(c) + 1)
