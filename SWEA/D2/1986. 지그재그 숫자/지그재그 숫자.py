T=int(input())
for i in range (1,T+1):
    N=int(input())
    if N%2==0:
        ans=(N//2)*-1
        print(f'#{i} {ans}')
    else:
        ans=(N//2)*-1+N
        print(f'#{i} {ans}')
     