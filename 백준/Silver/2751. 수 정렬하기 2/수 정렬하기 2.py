import sys
N=int(sys.stdin.readline())
x=[None]*N
for i in range(N):
    x[i]=int(sys.stdin.readline())
for j in sorted(x):
    print(j)