T = int(input())
N = int(input())
A = list(map(int, input().split(' ')))
M = int(input())
B = list(map(int, input().split(' ')))
if N < M:
    print('no')
    exit()
flag = [True] * len(A)
A.sort(reverse=True)
B.sort(reverse=False)
for j in range(len(B)):
    idx = -1
    for i in range(len(A)):
        if B[j] >= A[i] and flag[i] and B[j] - A[i] <= T:
            idx = i
    if idx == -1:
        print('no')
        exit()
    else:
        flag[idx] = False
print('yes')
