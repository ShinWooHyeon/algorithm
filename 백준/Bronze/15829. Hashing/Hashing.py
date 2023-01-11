from string import ascii_lowercase

alp=list(ascii_lowercase)
x={}
for i in range(26):
    x[alp[i]]=i+1

a=int(input())
b=input()
s=0
for k in range(len(b)):
    s+=x[b[k]]*(31**k)

print(s)    