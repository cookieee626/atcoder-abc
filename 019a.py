a = [['O', '0'],
    ['D', '0'],
    ['I', '1'],
    ['Z', '2'],
    ['S', '5'],
    ['B', '8']]
s = input()
for i in a:
    s = s.replace(i[0], i[1])
print(s)