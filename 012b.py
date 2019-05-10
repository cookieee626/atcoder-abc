N = int(input())
t = N // 3600
tmp_m = N % 3600
m = tmp_m // 60
s = tmp_m % 60
print('{0:0=2}:{1:0=2}:{2:0=2}'.format(t, m, s))