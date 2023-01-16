N=int(input())
x=list(map(int,input().split()))
c=0
p=0
for i in x:
    if i==1:
        c+=1
    else:
        c=0
    p+=c
print(p)