T=int(input())
for i in range(T):
    x=list(input())
    if len(x)%2!=0:
        print('NO')
    else:
        while True:    
            if x[0]=='(' and x[-1]==')':
                a=x.index(')')
                del_1=x.pop(a-1)
                del_2=x.pop(a-1)
                if len(x)==0:
                    print('YES')
                    break
            else:
                print('NO')
                break