import sys
input=sys.stdin.readline
N=int(input())
for i in range(N):
    x=(N-i)*'*'
    print(x.rjust(N))
    