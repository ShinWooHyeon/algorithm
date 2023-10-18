from collections import deque

inf = int(1e9)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 시작 좌표 찾고 방문처리 한다, 
def solution(board):
    h = len(board)
    w = len(board[0])
    visited = [[inf for _ in range(w)] for _ in range(h)]
    for i in range (h):
        for j in range(w):
            if board[i][j] == 'R':
                x , y = i, j
    for i in range (h):
        for j in range(w):
            if board[i][j] == 'G':
                gx , gy = i, j
    
    q= deque()
    visited[x][y] = 0
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True :
                if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != 'D':
                    nx += dx[i]
                    ny += dy[i]
                else:
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                    
            # 이동전 좌표 x, y 움직였을때의 좌표  nx, ny 생성
            if visited[x][y] + 1 < visited[nx][ny] :
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    # 위 과정을 돌면 로봇에서 출발해 도착할 수 있다면 거리로 바뀌고 아니면 inf 일것이다
    if visited[gx][gy] != inf:
        return visited[gx][gy]
    else:
        return -1