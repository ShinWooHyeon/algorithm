# 플로이드
# n개의 도시 m개의 버스 도시 a에서 b로 가는 필요한 비용의 최솟값 
import sys
input =sys.stdin.readline
n = int(input())
m = int(input())
inf = int(1e9)

graph= [[inf]* (n+1) for _ in range (n+1)]

for _ in range (m):
    a, b, c = map(int, input().strip().split())
    if graph[a][b] > c:
        graph[a][b] = c
for i in range (1, n + 1):
    graph[i][i] = 0

# 플로이드 워셜 
for k in range (1, n + 1):
    for a in range (1, n + 1):
        for b in range (1, n + 1):
            graph[a][b] = min(graph[a][b] ,graph[a][k] + graph[k][b])

for i in range (1, n+1):
    for j in range (1, n+1):
        if graph[i][j] == inf :
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
