import sys
input=sys.stdin.readline
for i in range (2):
    print(sum(sorted([int(input()) for _ in range (10)],reverse=True)[:3]), end=' ')