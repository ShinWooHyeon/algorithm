from copy import deepcopy
R, C, M = map(int,input().split())
board = [[0]*C for _ in range(R)]

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    board[r-1][c-1] = [s,d,z]

# 낚시왕 이동 -> 낚시왕 있는 열에서 가장 위에 있는 즉 행번호가 가장 작은 상어 잡는다 , 상어 사라진다 => 상어가 이동한다
ans = 0
# 위 -1,0 / 아래- 1,0 / 오른 0,1 / 왼 1,0
dir = [[-1,0], [1,0], [0 ,1], [0,-1]]

def outrange(i, j, fast, d):
    # 상어의 정보를 입력받고 다음 위치가 어디인지 계산해야 한다 범위가 넘을 수 있기 때문에
    dx, dy = dir[d -1] #1,2,3,4 니까 인덱스로 바꾸고 방향 표현
    if d == 1 or d == 2: # 행이 바뀐다 # 이동거리의 2배 하면 자기 자신이 나오니까
        fast = fast %((R -1) * 2)
    elif d==3 or d==4 :
        fast = fast %((C-1) * 2)
    while True:
        # fast가 나머지 이동할 거리인데 그게 만약 범위 안이라면 fast는 어차피 항상 고정이니까 굳이 반환 안해도 된다
        if 0 <= i + dx * fast < R and 0 <= j + dy * fast < C :
            return (i + dx* fast, j + dy * fast, d)
        
        # 만약 위 조건을 충족을 못 시켰을 경우
        if d == 1:
            # 0번인덱스~ i번 인덱스 까지 이동거리 i를 남은 fast에서 빼준다 
            fast -= i
            # 방향도 바뀌어야 하고 dx, dy도 바뀌어야한다 , 현재 0번인덱스가 된다
            d = 2       
            dx, dy = 1, 0
            i = 0

        elif d == 2:
            fast -= (R-1-i)
            d = 1
            dx, dy = -1, 0
            i = R- 1

        # 오른쪽 이동을 왼쪽 이동으로 바꿔야하니까
        elif d == 3:
            fast -= (C-1-j)
            d = 4
            dx, dy =  0, -1
            j = C- 1    
        elif d == 4:
            fast -= j
            d = 3
            dx, dy = 0, 1
            j = 0    


# 낚시꾼이 상어를 잡는다
for j in range (C):
    # 위 for문 자체가 시간 C초 동안 1초 사이클을 의마히기도 한다
    for i in range (R):
        # 열을 기준으로 내려간다 만약 발견하면 break
        if board[i][j] != 0:
            ans += board[i][j][2]
            board[i][j] = 0
            break
    # 상어가 이동한 board를 기록해야 한다
    new_board = [[0] * C for _ in range (R)]
    # board에 상어가 있다면 이동시킨다
    for i in range (R):
        for j in range (C):
            if board[i][j] != 0:
                fast = board[i][j][0]
                # i, j에서 fast를 가지고 이동한 결과가 다음 nx, ny가 된다 fast는 고정
                nx, ny, d = outrange(i, j, fast, board[i][j][1])
                #새로운 baord에 상어를 기록해야한다, 이때 상어가 있는지 없는지 중요하다
                if new_board[nx][ny] == 0:
                    new_board[nx][ny] = [fast, d, board[i][j][2]]
                else:
                    # 원래 있던놈보다 현재 물고기 사이즈가 크면 갱신한다
                    if new_board[nx][ny][2] < board[i][j][2]:
                        new_board[nx][ny] = [fast, d, board[i][j][2]]
    # 다음 for문 들어가기전 deepcopy를 한다
    board = deepcopy(new_board)


print(ans)