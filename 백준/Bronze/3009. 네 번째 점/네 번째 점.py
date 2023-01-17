import sys
a=[]
b=[]
for i in range(3):
    c,d=map(int,sys.stdin.readline().split())
    a.append(c)
    b.append(d)
for j in a:
    if a.count(j)==1:
        ans_x=j
for k in b:
    if b.count(k)==1:
        ans_y=k
print(ans_x,ans_y)