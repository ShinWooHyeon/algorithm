n=int(input())
s1='666'
c=0
while True:
    if '666' in s1:
        c+=1
    if c==n:
        print(s1)
        break
    s1=str(int(s1)+1)