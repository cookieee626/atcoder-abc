import math
N = int(input())
a = list(map(int, input().split(" ")))
while 0 in a:
    a.remove(0)
ave = sum(a) / len(a)
print(math.ceil(ave))