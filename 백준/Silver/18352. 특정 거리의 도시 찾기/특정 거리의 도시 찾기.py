# 특정 거리의 도시 찾기
from collections import deque
import sys
input =sys.stdin.readline
n, m, k, x = map(int, input().split())

# 돌다가 재방문 할경우 문제 생길 수 있으므로 False가 아니라 -1로 표시
visited = [-1] * (n+1)
graph=[[]  for _ in range (n+1)]
for _ in range (m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, start, visited):
    queue= deque([start])
    visited[start]= 0
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if visited[i]==-1:
                visited[i]=visited[q] + 1
                queue.append(i)

bfs(graph,x,visited)
city_list=[]
cnt=0
for i in range(1, n+1):
    if visited[i] == k:  
        city_list.append(i)
        cnt+=1
city_list.sort()

if cnt ==0:
    print(-1)
else: 
    for i in city_list:
        print(i)
