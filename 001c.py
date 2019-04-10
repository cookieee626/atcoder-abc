import sys
deg, dis = [int(x) for x in input().split()]
if 0 > deg <= 3600 or 0 > dis <= 12000:
    sys.exit()

dir=['N', 'NNE', 'NE', 'ENE',
     'E', 'ESE', 'SE', 'SSE',
     'S', 'SSW', 'SW', 'WSW',
     'W', 'WNW', 'NW', 'NNW']
edge = [x+112 for x in range(0, 3600, 225)]
diff = -1 if deg in edge else 0
#print(deg, diff)
#deg = deg - 112
print(deg)
idx_dir = int((deg - 112) / 225) + 1 if deg >= 112 else 0
print(idx_dir)
if idx_dir == 16:
    idx_dir = 0

dis = dis / 60
w = 0
if 3 <= dis <= 15:
    w = 1
elif 16 <= dis <= 33:
    w = 2
elif 34 <= dis <= 54:
    w = 3
elif 55 <= dis <= 79:
    w = 4
elif 80 <= dis <= 107:
    w = 5
elif 108 <= dis <= 138:
    w = 6
elif 139 <= dis <= 171:
    w = 7
elif 172 <= dis <= 207:
    w = 8
elif 208 <= dis <= 244:
    w = 9
elif 245 <= dis <= 284:
    w = 10
elif 285 <= dis <= 326:
    w = 11
else:
    w = 12

print(dir[idx_dir] + ' ' + str(w))
