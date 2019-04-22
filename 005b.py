N = int(input())
t = 100
for i in range(N):
  tmp = int(input())
  t = tmp if t > tmp else t
print(t)
