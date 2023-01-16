x=list(map(int,input().split()))
if len(set(x))==1:
    print(10000+1000*x[0])
elif len(set(x))==2:
    for i in x:
        if x.count(i)==2:
            print(1000+100*i)
            break
else:
    print(100*max(x))