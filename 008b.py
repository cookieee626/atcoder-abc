N = int(input())
S = {}
for i in range(N):
    k = input()
    S[k] = S.get(k, 0) + 1
print(max(S, key=S.get))
