r = 0
N, K = list(map(int, input().split(" ")))
R = list(map(int, input().split(" ")))
t = sorted(R, reverse=True)[:K]
for i in t[::-1]:
    r = (r + i) / 2
print(r)
