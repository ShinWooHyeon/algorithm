from collections import deque
import copy
n , m = map(int, input().split())
graph = [] # 초기 맵
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue=deque()
    temp_graph=copy.deepcopy(graph)
    
    # 바이러스 확인 후 삽입
    for i in range (n):
        for j in range (m):
            if temp_graph[i][j] == 2:
                queue.append((i,j))
    
    # 큐에는 지금 처음 바이러스 위치 다 저장되어있다
    while queue:
        x, y = queue.popleft()
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m :
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] =2
                    queue.append((nx, ny))

    global answer # max값을 기록할 지표
    cnt = 0  
    for i in range (n):
        cnt += temp_graph[i].count(0)

    answer =max (answer, cnt)

 # 재귀함수를 통해서 모든 지점에 대해서 벽 3개가 세워질 때를 고려할 수 있다
def makewall (cnt) :
    # 벽 3개가 세워지면 바이러스를 퍼트리도록 한다 
    if cnt == 3:
        # bfs로 바이러스를 퍼트린다
        bfs()
        return
    
    for i in range (n):
        for j in range (m):
            if graph[i][j] ==0: # 빈칸이라면
                graph[i][j] =1 # 벽을 세우고
                makewall( cnt + 1) # 벽의 개수를 1개 늘리고 확인한다
                graph[i][j] = 0 # i,j에 세운 벽을 다시 허문다 
for i in range (n):
    graph.append(list(map(int, input().split())))
answer = 0 # 초기값을 0으로 설정해 갱신
makewall(0) #초기 벽의 개수를 0 으로 설정해서 3까지 증ㄱ가시킨다다
print(answer)