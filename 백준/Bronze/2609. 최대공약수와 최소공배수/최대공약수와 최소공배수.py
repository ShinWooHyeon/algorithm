a,b=map(int,input().split())
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        m=i
x=a//m
y=b//m
z=x*y*m
print(m)
print(z)