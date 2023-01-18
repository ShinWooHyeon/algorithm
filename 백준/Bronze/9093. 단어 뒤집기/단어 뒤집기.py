import sys
T=int(sys.stdin.readline())
for i in range(T):
    x=sys.stdin.readline().split()
    for i in range(len(x)):
        x[i]=x[i][::-1]
    print(*x)        