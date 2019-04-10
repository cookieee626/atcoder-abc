N = int(input())
if 4 <= N <= 100:
    m = 0
    for i in range(N):
        m = m + (i + 1) * 10000
    print(m//N)

