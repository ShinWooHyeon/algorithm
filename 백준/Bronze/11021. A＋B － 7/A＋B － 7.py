T=int(input())
for i in range (1,T+1):
    x=list(map(int,input().split()))
    print(f'Case #{i}: {sum(x)}')