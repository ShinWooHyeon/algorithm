N=int(input())
x=[None]*N
for i in range(N):
    x[i]=int(input())
if x.count(1)>x.count(0):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')