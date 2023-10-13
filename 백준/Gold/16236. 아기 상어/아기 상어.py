import heapq

n = int(input())
graph = [list(map(int, input().split())) for _ in range (n)]
for i in range (n):
    for j in range (n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            sx = i
            sy = j

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    size= 2
    eat = 0
    time = 0 
    q=[]
    heapq.heappush(q, (0, sx, sy))
    visited =[[False] * n for _ in range (n)]
    while q:
        dist, x, y = heapq.heappop(q)
        # 자기 장소에 먹을 수 있는 고기가 있다면 (dist 기록하는 건 아래에서)
        # 큐에서 뽑은건 일반적으로 거리 계산후 최소 거리에 먹이가 있는 경우를 넣은 거니까
        # 빈칸이 아니면서 물고기려면 0보다 커야한다
        if 0 < graph[x][y] < size :
            graph[x][y] = 0
            eat += 1
            if eat == size:
                size += 1
                eat = 0 
            # 고기를 먹으러 이동한 것이니까 도착한 순간 q의 정보는 전부 필요가 없어졌고 새로 갱신되야 함
            # 처음부터 시작하는거니까 즉 기준점의 dist는 다시 0이 되야 한다 
            time += dist
            dist =0 
            q.clear()
            
            # 
            visited =[[False] * n for _ in range (n)]
        # 고기 찾을 때 까지 1칸씩 이동하면서 그걸 heapq에 넣는 방식으로 진행하는 것이다
        # 고기 찾았으면 거리 0 근데, 고기 찾으러 한 칸씩 이동중인 큐를 꺼냈다면 기존 dist에 +1을 해야한다 
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = dist + 1
            # 방문여부와 이동할 수 있는 칸인지 확인한다
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= size and not visited[nx][ny]:
                heapq.heappush(q, (nd, nx, ny))
                visited[nx][ny] = True
    print(time)

bfs()