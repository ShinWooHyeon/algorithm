import sys
input=sys.stdin.readline
N=int(input())
five_cnt=N//5
while five_cnt:
    if (N-(five_cnt*5))%3!=0:
        five_cnt-=1
        continue
    else:
        three_cnt=(N-five_cnt*5)//3
        print(five_cnt+three_cnt)
        break
if five_cnt==0:
    if N%3!=0:
        print(-1)
    else:
        print(N//3)