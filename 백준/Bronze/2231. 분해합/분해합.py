x=int(input())
for i in range(x):
    s=0
    a=i
    while True:    
        b=a%10
        s+=b
        a//=10
        if a==0:
            break
    if i+s==x:
        print(i)
        break
else:
    print(0)