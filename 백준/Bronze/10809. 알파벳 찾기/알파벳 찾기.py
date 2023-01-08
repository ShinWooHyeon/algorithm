from string import ascii_lowercase
al=list(ascii_lowercase)
x=input()
for i in range(len(al)):
    for k in x:
        if al[i]==k:
            al[i]=x.index(k)
            break
    else:
        al[i]=-1

for i in al:
    print(i,end=' ')
    
    