import sys
m = int(input())
if(0<=m<100):
    print('{0:02d}'.format(0))
elif(100<=m<=5000):
    print('{0:02d}'.format(m//100))
elif(6000<=m<=30000):
    print(m//1000+50)
elif(35000<=m<=70000):
    print((m//1000-30)//5+80)
elif(70000<m):
    print(89)
else:
    sys.exit()