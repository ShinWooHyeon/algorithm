x=[[0]*100 for i in range(100)]
for j in range(4):
    a,b,c,d=map(int,input().split())
    for y_p in range(b,d):
        for x_p in range(a,c):
            x[y_p][x_p]=1
total=0
for k in x:
    total+=sum(k)
print(total)