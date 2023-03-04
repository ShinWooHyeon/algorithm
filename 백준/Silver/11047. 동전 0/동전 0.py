N, K = map(int, input().split()) 
coin = []
for _ in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)

ans = 0
for c in coin:
    if K >= c:
        ans += K // c
        K %= c 
        if K <= 0:
       		break
print(ans) 