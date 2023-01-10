T=int(input())
for t in range(1,T+1):
    x=list(map(int,input().split()))
    y=max(x)
    print(f'#{t} {y}')