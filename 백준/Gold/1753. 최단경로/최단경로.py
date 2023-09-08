# 백준 최단경로
import sys
import heapq
input =sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
inf = 1e9
# 거리담을 리스트
distance =[inf] * (v + 1)


# 그래프를 입력받는다
graph= [[] for _ in range (v+1)]

for i in range (e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라를 정의한다
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist +i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(k)
for i in range (1, v+1):
    if distance[i] != inf:       
        print(distance[i])
    else:
        print('INF')