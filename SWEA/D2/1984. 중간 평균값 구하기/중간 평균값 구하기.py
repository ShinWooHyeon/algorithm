
T=int(input())
for i in range (1,T+1):
    x=list(map(int,input().split()))
    ans=round((sum(x)-max(x)-min(x))/8)
    print(f'#{i} {ans}')