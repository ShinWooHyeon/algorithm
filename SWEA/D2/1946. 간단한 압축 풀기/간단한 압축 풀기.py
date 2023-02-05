T=int(input())
for i in range(1,T+1):
    N=int(input())
    x=''
    for j in range (N):
        a,b=input().split()
        x+=a*int(b)
    print(f'#{i}')
    cnt=(len(x)-1)//10
    for k in range(cnt+1):
        print(x[10*k:10*(k+1)])
