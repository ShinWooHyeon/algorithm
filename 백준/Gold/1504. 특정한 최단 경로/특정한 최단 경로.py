import sys
import heapq
input = sys.stdin.readline
INF = 2147000000

# ✨ 입력
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,input().split())

# ✨ dijkstra 함수
def dijkstra(start,end):
    dist = [INF]*(N+1)
    dist[start] = 0
    hq = [(0,start)]
    while hq:
        len,node = heapq.heappop(hq)
        if len > dist[node]:
            continue
        for next_node, val in graph[node]:
            if dist[next_node] > dist[node] + val:
                dist[next_node] = dist[node]+val
                heapq.heappush(hq,(dist[next_node],next_node))
    return dist[end]

# ✨ 경로 설정
path1 = dijkstra(1,v1) + dijkstra(v1, v2) + dijkstra(v2,N)
path2 = dijkstra(1,v2) + dijkstra(v2, v1) + dijkstra(v1,N)

# ✨ 출력
print(-1) if path1 >= INF and path2 >= INF else print(min(path1,path2))