for _ in range (10):
    i=int(input())
    tc=list(map(int,input().split()))
    while tc[-1]>0:
        for j in range(1,6):
            tc=tc[1:]+[tc[0]-j] 
            if tc[-1]<=0:
                tc[-1]=0
                print(f'#{i}',end=' ')
                print(*tc)
                break