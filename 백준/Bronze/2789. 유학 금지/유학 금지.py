import sys
a='CAMBRIDGE'
b=list(a)
x=sys.stdin.readline()
c=''
for i in x:
    if i not in b: 
        c+=i
print(c)