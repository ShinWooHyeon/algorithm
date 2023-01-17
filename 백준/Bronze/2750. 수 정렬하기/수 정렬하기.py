import sys
N=int(sys.stdin.readline())
x=[None]*N
for i in range(N):
    x[i]=int(sys.stdin.readline())
for i in sorted(x):
    print(i)