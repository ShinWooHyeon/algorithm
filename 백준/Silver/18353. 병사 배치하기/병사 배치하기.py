# 병사 배치하기
# 가장 긴 증가하는 부분수열
# 다이나믹 프로그래밍 D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대길이 
# 모든 DP 테이블의 값을 1로 초기화 한다 # 길이중 1개 포함하면 1 증가하니까 
# 점화식은 0<= j < i 에 대해서 D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
# j 까지 증가하고 i가 j보다 클경우 길이가 1증가하는것인데 다른 j로 연결되었을 때가 더 클경우 갱신이 안된다는 의미이다

n = int(input())
array = list(map(int, input().split()))
# 가장 긴 감소하는 부분 수열은 뒤집어서 가장 긴 증가하는 부분수열로 해결 할 수 있다
array.reverse()

dp=[1] * (n)

for i in range (n):
    for j in range (0,i):
        if array[j] < array[i]:
            dp[i]= max(dp[j] +1, dp[i])

print(n-max(dp))