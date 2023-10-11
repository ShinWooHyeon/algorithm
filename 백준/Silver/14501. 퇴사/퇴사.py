# 백준 퇴사
# 동적프로그래밍, n일차에 얻는 수익을 지속적으로 갱신한다
n = int(input())
dp = [0] * (n + 1)
for i in range (1, n + 1):
    t, p = map(int, input().split())
    # 자신의 날짜에 dp 값과 자기 앞 값의 수치 중 더 큰 값을 dp 값으로 가진다
    dp[i] = max(dp[i], dp[i-1])
    # i + t일이 끝나고 얻는 수익은 기존에 dp에 기록되어있는 값과 현재 날짜까지 수익 + 일하고 얻는 수익 중 큰 값으로 갱신
    
    if (i + t - 1) <= n   :
        dp[i + t - 1] = max( dp[i-1]+ p, dp[i + t - 1])
print(max(dp))