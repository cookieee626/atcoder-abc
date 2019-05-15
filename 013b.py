a = int(input())
b = int(input())

diff = abs(a-b)
if diff <= 5:
    print(diff)
else:
    max, min = [a, b] if a > b else [b, a]
    print(9 - max + min + 1)
    

#0 1 2 3 4 5 6 7 8 9