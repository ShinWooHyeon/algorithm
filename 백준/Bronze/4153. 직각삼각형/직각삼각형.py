while True:
    x=list(map(int,input().split()))
    if x==[0,0,0]:
        break
    else:
        a=max(x)
        x.remove(a)
        s=0
        for i in x:
            s+=i**2
        if a**2==s:
            print('right')
        else:
            print('wrong')