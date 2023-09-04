# 정수삼각형
n = int(input())
dp=[]
for i in range (n):
    if i != n-1:
        line=[0] * (n-1-i)
    else:
        line=[]
    line.extend(list(map(int, input().split()))) 
    dp.append(line)

# 바텀 업 방식으로 dp 진행

for i in range (1, n):
    for j in range(n):
        # 바로위 혹은 대각선 오른쪽 위에서 내려오는 경우 밖에 없다 
        if j == n-1:
            right_up = 0
        else:
            right_up = dp[i-1][j + 1]
        up = dp[i-1][j]
        dp[i][j] = max(right_up, up) + dp[i][j]

print(max(dp[n-1]))       