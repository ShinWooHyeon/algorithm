import sys
input=sys.stdin.readline
A,B=input().split()
a=map(int,list(A))
b=map(int,list(B))
print(sum(a)*sum(b))