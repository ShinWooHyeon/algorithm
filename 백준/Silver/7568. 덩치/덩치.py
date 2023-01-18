import sys
N=int(sys.stdin.readline())
x=[None]*N
for i in range (N):
   x[i]=list(map(int,sys.stdin.readline().split()))
for i in x:
    c=0
    for j in x:
        if (j[0]>i[0]) and j[1]>i[1]:
            c+=1
    print(c+1,end=' ')     