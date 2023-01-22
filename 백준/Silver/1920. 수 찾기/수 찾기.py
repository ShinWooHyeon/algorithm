import sys
N = int(sys.stdin.readline())
X = set(map(int, sys.stdin.readline().split()))	
M = int(sys.stdin.readline())
Y = list(map(int, sys.stdin.readline().split()))
for i in Y:
    print (1) if i in X else print(0)  