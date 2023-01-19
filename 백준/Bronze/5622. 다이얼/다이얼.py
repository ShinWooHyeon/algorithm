import string
alph=list(string.ascii_uppercase)
x=input()
s=0
for i in x:
    num=alph.index(i)
    if num<=14:
        s+=num//3+3
    else:
        if i in ['P','Q','R','S']:
            s+=8
        elif i in ['T','U','V']:
            s+=9
        else:
            s+=10
print(s)