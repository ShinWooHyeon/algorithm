import sys
from collections import deque
input=sys.stdin.readline
T=int(input())
for _ in range (T):
    N,M=map(int,input().split())
    file=deque(list(map(int,input().split())))
    cnt=0
    while file:
        out_num=max(file)
        try_num=file.popleft()
        M-=1
        if try_num==out_num:
            cnt+=1
            if M<0:
                print(cnt)
                break
        else:
            file.append(try_num)
            if M<0:
                M=len(file)-1