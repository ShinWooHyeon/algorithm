import sys
from collections import Counter
input=sys.stdin.readline
N=int(input())
x=[int(input()) for _ in range(N)]
x.sort()
cnt=Counter(x).most_common(2)
print(round(sum(x)/len(x)))
print(x[N//2])
if len(x)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(x)-min(x))