# 모든 회전 방향과 
# 이동은 무조
# 어떻게 이동해야 할까 ? bfs로 그 전까지의 시간 기록 하고 회전, 이동시 다음 블럭의 시간=그전시간+1
# 맵을 확장하고 외곽에 벽을 둔다면 범위 설정시 편하게 풀이 가능하다 
from collections import deque
def get_next_pos(pos, board):
    next_pos = [] # 이동가능한 위치들
    pos = list(pos) # 현재 위치 정보를 변환 ,2가지 좌표이며 집합으로 설정했음, 중복막기 위해 
    pos1_x , pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 먼저 상하좌우 운동에 대해 정의
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range (4) :
        pos1_nx, pos1_ny, pos2_nx, pos2_ny = pos1_x + dx[i], pos1_y + dy[i] , pos2_x + dx[i], pos2_y + dy[i]
        # 이동한 좌표가 모두 0이여야 이동가능하다  (좌우이동시 어떻게될지느 추후 처리)
        # 확장시킬 경우 이렇게 하면 nx,ny 등의 범위를 고려하지 않아도 된다
        if board[pos1_nx][pos1_ny] == 0 and board[pos2_nx][pos2_ny] == 0 :
            # 집합 형태로 붙여야한다
            # next_pos는 이동가능한 좌표들을 일단 모아놓은 곳
            next_pos.append({(pos1_nx, pos1_ny), (pos2_nx, pos2_ny)})
    # 현재 로봇이 어떻게 위치해있는지 가로or 세로 , x가 높이를 의미하는 것을 까먹지 말자
    # 가로인 경우 위쪽으로 회전, 아래쪽으로 회전 가능하다 
    if pos1_x == pos2_x :
        for i in [-1, 1]:
            # -1일경우 위가 비어있을경우 1일 경우 아래가 비어있을 경우로 해석 가능하다
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0 :
                # 행은 pos1
                next_pos.append({(pos1_x , pos1_y) ,(pos1_x +i, pos1_y)})
                next_pos.append({(pos2_x , pos2_y) ,(pos2_x +i, pos2_y)})
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            # -1일경우 위가 비어있을경우 1일 경우 아래가 비어있을 경우로 해석 가능하다
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0 :
                # 
                next_pos.append({(pos1_x , pos1_y) ,(pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x , pos2_y) ,(pos2_x, pos2_y + i)}) 
    # 이동가능한 모든 위치를 반환한다
    return next_pos

def solution (board):
    # 맵 외곽에 한개의 벽 (1)을 더 둘러 쌓는다
    n = len(board)
    new_board = [[1] * (n+2) for _ in range (n+2)]
    for i in range (n):
        for j in range (n):
            new_board[i+1][j+1] = board[i][j]
    # bfs 수행
    q = deque()
    visited=[]
    pos={(1,1), (1,2)}
    q.append((pos, 0))  # 여기서 0은 거리를 계산하기 위한 수치
    visited.append(pos)
    while q:
        pos, cost = q.popleft() # 현재 좌표와 비용
        # n,n에 도달했으면 거리를 반환한다
        if (n,n) in pos:
            return cost
        
        # pos 에서 이동할 수 있는 위치를 확인하고 그 좌표들을 for문을 돌린다
        for next_pos in get_next_pos (pos, new_board) : 
            # 방문 안한 좌표라면 큐에 삽입해 모든 좌표를 bfs로 방문처리 한다
            # 그렇게 방문처리 하던 도중 n,n에 도달했을 때 cost를 확인한다!
            if next_pos not in visited :
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0