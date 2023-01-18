import sys
x=list(map(int,(sys.stdin.readline().split())))

while True:
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            x[i],x[i+1]=x[i+1],x[i]
            print(*x)
    if x==[1,2,3,4,5]:
        break