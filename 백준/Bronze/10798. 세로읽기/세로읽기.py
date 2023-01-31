import sys
input=sys.stdin.readline
x=[]
for i in range(5):
    text=list(input().strip())
    total_text=text+['']*(15-len(text))
    x.append(total_text)
for j in range (15):
    for k  in range(5):
        print(x[k][j],end='')