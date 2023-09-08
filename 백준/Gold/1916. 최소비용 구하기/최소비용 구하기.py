# 최소비용 구하기
import sys
import heapq
input = sys.stdin.readline
inf = 1e9
# 도시의 개수 입력받기
n = int(input())

# 간선의 개수 입력받기
m = int(input())

# 거리 리스트 생성
distance = [inf] * (n + 1)
# 그래프 입력받기
graph=[[] for _ in range (n + 1)]
for i in range (m) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 출발도시와 목적기 입력받기
start, end = map(int, input().split())

# 출발도시의까지의 거리는 0으로 정의
distance[start] = 0
# 다익스트라 정의
def dijkstra(start):
    q=[]
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance[end])