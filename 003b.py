S = str(input())
T = str(input())
ref = ['a', 't', 'c', 'o', 'd', 'e', 'r']
flag = True

for s, t in zip(list(S), list(T)):
    if s != t:
        if not (s in ref and t == '@' or t in ref and s == '@'):
            flag = False

if flag:
    print('You can win')
else:
    print('You will lose')
