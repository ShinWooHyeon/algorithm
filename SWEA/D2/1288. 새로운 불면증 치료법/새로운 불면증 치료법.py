T=int(input())
for i in range(1,T+1):
    a=int(input())
    b=[]
    n=1
    while True:
        x=str(a*n)
        for k in x:
            if k not in b:
                b.append(k) 
        if len(b)==10:
            print(f'#{i} {int(x)}') 
            break
        else:
            n+=1
