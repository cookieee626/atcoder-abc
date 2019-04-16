c = [input().split()]
c.append(input().split())
c.append(input().split())
c.append(input().split())
res = []
for tmp in c[::-1]:
    print('{0[0]} {0[1]} {0[2]} {0[3]}'.format(tmp[::-1]))


