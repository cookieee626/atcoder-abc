a, b, c = list(map(int, input().split(" ")))
p = a + b
d = a - b
if p == c and d == c:
    print('?')
elif p == c:
    print("+")
elif d == c:
    print('-')
else:
    print('!')