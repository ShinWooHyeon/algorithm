a,b=map(int,input().split())
x=list(map(int,input().split()))
n=0
y=0
while n <=(len(x)-3):
    for i in range(n+1,len(x)-1):
        for j in range(i+1,len(x)):
            s=x[n]+x[i]+x[j]
            if s<=b and s>=y:
                y=s
            if y==b:
                break
        if y==b:
            break
    if y==b:
        break
    n+=1
print(y)    