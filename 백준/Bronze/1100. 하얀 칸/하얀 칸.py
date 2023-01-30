import sys
input=sys.stdin.readline
x=[list(input().strip())for i in range (8)]
cnt=0
for i in range(8):
    for j in range(8):
        if i%2==0 and j%2==0:
            if x[i][j]=='F':
                cnt+=1
        if i%2==1 and j%2==1:
            if x[i][j]=='F':
                cnt+=1
print(cnt)     