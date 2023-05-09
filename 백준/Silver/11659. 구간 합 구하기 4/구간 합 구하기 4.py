import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(n):
    dp[i + 1] = dp[i] + num_list[i]

for j in range(m):
    x, y = map(int, input().split())
    print(dp[y] - dp[x - 1])