T=int(input())
for t in range(1,T+1):
    x=list(map(int,input().split()))
    avg=round(sum(x)/len(x))
    print(f'#{t} {avg}')