A = [0, 0, 1]
n = int(input())
tmp=10007
for i in range(3, n):
    A[i%3] = sum(A[:])%tmp
print(A[(n-1)%3])

