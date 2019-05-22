a, b = list(map(abs, map(int, input().split(" "))))
if a == b:
    print('Draw')
elif a < b:
    print('Ant')
else:
    print('Bug')