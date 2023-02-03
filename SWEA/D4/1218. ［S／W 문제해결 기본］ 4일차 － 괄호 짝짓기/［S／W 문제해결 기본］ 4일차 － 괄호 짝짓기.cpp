T=10
oc=['(',')','[',']','{','}','<','>']
for i in range(1,T+1):
    length=int(input())
    open_close=list(input().strip())
    for j in range(4):
        if open_close.count(oc[2*j])!=open_close.count(oc[2*j+1]):
            print(f'#{i}',end=' ')
            print(0)
            break
    else:
        print(f'#{i}',end=' ')
        print(1)