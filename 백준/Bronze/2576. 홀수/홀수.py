import sys
s=0
m=100
for i in range (7):
    x=int(sys.stdin.readline())
    if x%2==1:
        s+=x
        if x<m:
            m=x
if m==100:
    print(-1)           
else:
    print(s)
    print(m)        