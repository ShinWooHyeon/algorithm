from string import ascii_lowercase
alp=list(ascii_lowercase)
a=int(input())
b=input()
s=0
for k in range(len(b)):
    s+=(alp.index(b[k])+1)*(31**k)
print(s)    
