N=int(input())
X=['3','6','9']
for i in range(1,N+1):
    cnt=0
    for j in X:
        cnt+=str(i).count(j)
    if cnt==0:
        print(i,end=' ')
    else:
        print('-'*cnt,end=' ')