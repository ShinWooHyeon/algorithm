import sys
input=sys.stdin.readline
N,M=map(int,input().split())
chess=[list(input().strip()) for _ in range (N)]
min_draw=M*N
for i in range (N-7):
    for j in range (M-7):
        color=['B','W']
        color.remove(chess[i][j])
        other=color[0]
        cnt_1=0
        cnt_2=0
        for m in range (8):
            for n in range (8):
                if (m+n)%2==0:
                    if chess[i+m][j+n]!=chess[i][j]:
                        cnt_1+=1
                    else:
                        cnt_2+=1
                else:
                    if chess[i+m][j+n]!=other:
                        cnt_1+=1
                    else:
                        cnt_2+=1
        cnt=min(cnt_1,cnt_2)
        if cnt<min_draw:
            min_draw=cnt
print(min_draw)