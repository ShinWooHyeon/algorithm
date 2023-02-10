for i in range(1,11):
    n=int(input())
    boxlist=list(map(int,input().split()))
    if max(boxlist)==min(boxlist):
        print(f'#{i} 0')
        break
    for j in range(n):
        a=boxlist.index(max(boxlist))
        b=boxlist.index(min(boxlist))
        boxlist[a]-=1
        boxlist[b]+=1
    print(f'#{i}',end=' ')
    print(max(boxlist)-min(boxlist))