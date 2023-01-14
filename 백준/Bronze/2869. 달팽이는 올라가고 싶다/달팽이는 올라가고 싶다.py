a,b,v=map(int,input().split())
c=v-a
d=a-b
n= c//d
x= c%d
if x!=0:
    print(n+2)
else:
    print(n+1)