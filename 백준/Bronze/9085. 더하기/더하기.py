import sys
T=int(sys.stdin.readline())

for i in range(T):
    N=int(sys.stdin.readline())
    x=map(int,sys.stdin.readline().split())
    print(sum(x))