x=[]
for i in range (3):
    x.append(int(input()))
if sum(x)==180:
    if len(set(x))==1:
        print('Equilateral')
    elif len(set(x))==2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error') 