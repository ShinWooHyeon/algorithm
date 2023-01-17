import sys
N=int(sys.stdin.readline())
x=list(map(int,sys.stdin.readline().split()))
c=0
for i in x:
    cs=0
    for j in range(1,i+1):
        if i%j==0:
            cs+=1
    if cs==2:
        c+=1
print(c) 