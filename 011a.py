N = int(input())
N = (N + 1) % 12
if N == 0:
    print(12)
else:
    print(N)