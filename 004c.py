c = [1, 2, 3, 4, 5, 6]
N = int(input())
N = N % (6 * 5)
for i in range(N):
    a = (i % 5) + 1 - 1
    b = (i % 5) + 2 - 1
    c[a], c[b] = c[b], c[a]
print('{0[0]}{0[1]}{0[2]}{0[3]}{0[4]}{0[5]}'.format(c))