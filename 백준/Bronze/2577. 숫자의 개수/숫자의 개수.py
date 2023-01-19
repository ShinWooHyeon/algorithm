a=1
x=[0,1,2,3,4,5,6,7,8,9]
for i in range(3):
    b=int(input())
    a*=b
a=str(a)
for i in x:
    print(a.count(str(i)))