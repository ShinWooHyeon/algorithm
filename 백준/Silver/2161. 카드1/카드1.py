N=int(input())
x=list(range(1,N+1))
while x:
    print(x.pop(0),end=' ')
    x=x[1:]+x[0:1]
    