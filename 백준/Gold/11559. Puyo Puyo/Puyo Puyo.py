# dfs를 어떻게 적절하게 사용할것인가?
# 먼저 bfs로 처리해서 이 좌표에서 시작한bfs가 True면 그거 지우는거 
# vistited를 while문이 반복될 때마다 시행하는 것도 옳은 표현 
# 떨구는 함수는 구현 ok  
import sys
from collections import deque
input = sys.stdin.readline

# x,y 
# 확인하고자 하는 가능한 뿌요구간을 기록해야함
# 시작점을 방문처리하는 함수를 시작할때 
def bfs(x, y):
    q = deque([(x, y)])
    now = graph[x][y]
    pos = [] 

    while q:
        x, y = q.popleft()
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny <6 and graph[nx][ny] == now and not visited[nx][ny]:
                visited[nx][ny] = 1
                pos.append((nx, ny))
                q.append((nx, ny))
    if len(pos) >=4:            
        pos.sort(key=lambda x: (x[1], x[0]))        
        for i, j in pos:
            graph[i][j] = 'x'
            bomblist.append((i,j))
dx= [-1, 1, 0 , 0]
dy= [0, 0, -1, 1]
graph=[list(input().strip()) for _ in range (12)]
time = 0

while True:
    # 
    visited = [[0]* 6 for _ in range (12)]
    bomblist=[]
    # 색인 같은 뿌요들은 모두 
    for i in range(12):
        for j in range (6):
            if graph[i][j] != '.' and graph[i][j] !='x' and not visited[i][j]:
                bfs(i, j)
                # pos는 갱신되도 bomblist에 계속 붙여지므로 상관없음
    if len(bomblist) == 0:
        break
    # bfs 문에서 bomb 가능한 것은 전부 bomb 하고 뿌요를 내려야한다
    # 
    for bomb in bomblist:
        bx, by= bomb    
        for i in range (bx, 0, -1):
            graph[i][by]= graph[i-1][by]   
        graph[0][by] = '.'
    time += 1

print(time)