T=int(input())
x=[25,10,5,1]
for i in range (T):
    c=int(input())
    for k in x:
        if c//k!=0:
            print(c//k,end=' ')
            c=c%k
        else:
            print(0,end=' ')
        