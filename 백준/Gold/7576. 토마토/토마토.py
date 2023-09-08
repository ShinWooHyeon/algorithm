# 익은 토마토들의 인접한한  곳은 토마토 영향 받아 익는다
# bfs를 돌며 거리를 기록한다 
# 0인곳만 확산 가능하니까 
from collections import deque
m , n = map(int, input().split())
start=[]
graph=[]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
# 토마토가 표시된 그래프를 받고 , 익은 토마토의 인덱스를 받아 start에 넣어준다
# 마지막엔 맵 전체 돌며 최댓값 기록, 0이 1개도 없으면 max 출력 0이 1개라도 있으면 -1 출력
for i in range (n):
    line= list(map(int, input().split()))
    graph.append(line)
    for j in range (m):
        if line[j] == 1:
            start.append((i, j))
def bfs(graph, start):
    q=deque(start)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] ==0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
max_value= -1e9
fail =False
bfs(graph, start)
for i in range(n):
    for j in range (m):
        if graph[i][j] == 0:
            fail = True 
            break
        else:
            if graph[i][j] > max_value:
                max_value = graph[i][j]
    if fail :
        break

if not fail:
    print (max_value - 1)
else:
    print(-1)