n, s, t = list(map(int, input().split(" ")))
w = int(input())
count = 0
for i in range(n):
    if not i == 0:
        w = w + int(input())
    if s <= w <= t:
        count += 1
print(count)