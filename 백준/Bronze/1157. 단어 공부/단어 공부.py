a=input().upper()
b=[]
c={}
for i in a:
    if i not in b:
        b.append(i)
        c[i]=a.count(i)
d=[k for k,v in c.items() if v ==max(c.values())]
if len(d)==1:
    print(d[0])
else:
    print('?')
    
    