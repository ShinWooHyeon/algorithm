def solution(sequence):
    answer = 0
    # 시작이 -1일경우 / 1일 경우 일단 2가지가 있을 것인데 그냥 한개로 통일하고 최대 ,최소에 abs
    n = len(sequence)
    for i in range (n):
        if i%2 ==1:
            sequence[i] *= -1
    dp =[ [0,0] for _ in range (n)]
    dp[0] = [sequence[0], sequence[0]]
    
    for i in range (1, n):
        dp[i][0] = min(sequence[i], sequence[i] + dp[i-1][0])
        dp[i][1] = max(sequence[i], sequence[i] + dp[i-1][1])
    
    min_value = min(map(min, dp))
    max_value = max(map(max, dp))
    return max(abs(min_value), abs(max_value))