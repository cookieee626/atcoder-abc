N, M = list(map(int, input().split(" ")))
for baby in range(min(N, M//4)+1):
    adult = 3 * N - M + baby
    older = M - 2 * N - 2 * baby
    #print(adult, older, baby, adult+older+baby,adult*2+older*3+baby*4)
    #if adult >= 0 and older >= 0 and M == adult*2+older*3+baby*4:
    if adult >= 0 and older >= 0:
        print(adult, older, baby)
        exit()
print(-1, -1, -1)