import sys
T=int(sys.stdin.readline())
x=[None]*T
for i in range (T):
    x[i]=list(map(int,sys.stdin.readline().split()))
x.sort(key=lambda x:(x[1],x[0]))

for i in x:
    print(*i)
                