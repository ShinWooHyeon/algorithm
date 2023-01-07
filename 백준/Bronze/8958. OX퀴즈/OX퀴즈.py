#8958
for i in range(int(input())):
    x=input()
    j=0
    s=0
    for k in x:
        if k=='O':
            j+=1
            s+=j
        else:
            j=0
    print(s)