import sys
input=sys.stdin.readline
T=int(input())
for i in range (T):
    m,n=map(int,input().split())
    greed=[list(map(int,input().split()))for _ in range (m)]
    sum=0
    for j in range (n):
        cnt=0
        place=0
        for k in range(m):
            if greed[k][j]==1:
                cnt+=1
                place+=(m-k)
        sum+=int(place-(cnt*(cnt+1)/2))
    print(sum)