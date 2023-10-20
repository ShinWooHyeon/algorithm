def solution(x, y, n):
    answer = 0
    # 증가하기 때문에 1~40까지 만들고 
    dp = [1e9 for _ in range (y + 1)]
    dp[x] = 0
    for i in range (x, y + 1):
        if dp[i] != 1e9:
            if i + n <= y: 
                dp[i + n] =  min(dp[n + i], dp[i] + 1)
            if i * 2 <= y:
                dp[i * 2] =  min(dp[i * 2], dp[i] + 1) 
            if i * 3 <= y:
                dp[i * 3] =  min(dp[i * 3], dp[i] + 1)
    if dp[y] != 1e9:
        return dp[y]
    else:
        return -1