# 퇴사
# dp[i]를 i 번째 날 ~ n일 까지 얻을 수 있는 최대 이익으로 설정
n = int(input())
t = [] # 상담시간 정리
p = [] # 상담금액 정리
dp = [0] *(n+1)
max_value = 0

for _ in range (n) :
    x , y = map(int, input().split())
    t.append (x)
    p.append (y)


for i in range (n-1, -1, -1):
    time= t[i] + i # i는 인덱스이므로 날짜 -1이고 시간 t를 더하면 time은 i일의 상담이 끝난 다음 날 
    # 상담이 기간안에 끝난 경우 
    if time <= n: # 인덱스니까 끝난 다음날이 n+1일이므로 인덱스는 n까지 가능하다 
        # 현재까지의 최고 이익은 다음과 같이 계산 된다
        dp[i]= max(dp[time] +p[i] ,max_value)
        max_value= dp[i]
    else:
        dp[i] = max_value # 뭘 더 더하지 않고 그냥 현재까지 기록된 최댓값이다
    
print(max_value)