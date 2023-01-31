import sys
input=sys.stdin.readline
N=int(input())
room=[list(input().strip()) for _ in range (N)]
cnt_1=0
cnt_2=0
# 문제 예시에는 안 나와 있지만 ..xx..일 경우 2개니까 이걸 고려해야한다!!
for i in range (N):  
    for k in range (N-1): #가로부터확인
        if room[i][k]=='.'and room[i][k+1]=='.':
            if k==N-2:
                cnt_1+=1
            else:
                if room[i][k+2]!='.':
                    cnt_1+=1
    for j in range (N-1): # 세로 확인 
        if room[j][i]=='.'and room[j+1][i]=='.':
            if j==N-2:
                cnt_2+=1
            else:
                if room[j+2][i]!='.':
                    cnt_2+=1
print(cnt_1,cnt_2)
        