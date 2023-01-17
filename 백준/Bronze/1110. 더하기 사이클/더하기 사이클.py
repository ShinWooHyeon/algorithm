a=input()
n=1
sol=a
if int(a)>=10:
    while True:
        if int(a[0])+int(a[1])>=10:
            a=a[1] +str(int(a[0])+int(a[1]))[1]
            if a==sol:
                print(n)
                break
            else:
                n+=1
        else:
            a=a[1]+str(int(a[0])+int(a[1]))
            if a==sol:
                print(n)

                break
            else:
                n+=1
else:
    a='0'+a
    sol=a
    while True:        
        if int(a[0])+int(a[1])>=10:
            a=a[1] +str(int(a[0])+int(a[1]))[1]
            if a==sol:
                print(n)
                break
            else:
                n+=1
        else:
            a=a[1]+str(int(a[0])+int(a[1]))
            if a==sol:
                print(n)
                break
            else:
                n+=1
        