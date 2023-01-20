T=int(input())
for i in range (1,T+1):
    bdpq=list(input())
    x=bdpq[::-1]
    for k in range(len(x)):
        if x[k]=='b':
            x[k]='d'
        elif x[k]=='d':
            x[k]='b'
        elif x[k]=='p':
            x[k]='q'
        else:
            x[k]='p'  
    ans=''.join(x)
    print(f'#{i} {ans}')