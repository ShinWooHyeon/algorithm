import sys
input=sys.stdin.readline
T=int(input())
for _ in range (T):
    x=list(map(int,input().split()))
    max_point=max(x)
    min_pint=min(x)
    x.remove(max(x))
    x.remove(min(x))
    if max(x)-min(x)>=4:
        print('KIN')
    else:
        print(sum(x))
    