a=int(input())
for i in range(1,a+1):
    b=i *'*'
    c=b.rjust(a)
    print(c)