from copy import deepcopy
n, m = map(int, input().split())

cctv = []
graph = []
# 방향을 지정해줘야 맨처음 내가 풀었던 것 처럼 복잡한 코드 나오지 않는다
# 1개 인덱스(0번인덱스)를 추가해 각 번호별로 자기 방향 갖도록 한다 
mode= [
    [],
    [[0],[1],[2],[3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1 ,3], [0, 2, 3], [1, 2, 3]],
    [[0, 1, 2, 3]]
]

# 4 방향으로 움직일 때는 항상 dx, dy 행렬을 이용하자 북 동 남 서 0, 1, 2,3 이렇게 생각하고 만들자
dx = [-1, 0, 1, 0]
dy=  [0, 1, 0, -1]

# cctv의 위치와 graph를 입력받는다
# 이때 cctv의 정보도 담아 리스트 형태로 cctv에 저장한다
for i in range (n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range (m):
        if line[j] in [1, 2, 3, 4, 5] :
            cctv.append([line[j], i, j])

# office를 채우는 함수를 정의한다 
# 이때 해당 cctv의 mode도 받아 for문을 돌려 선택한 방향(여러방향일 수 있으므로)의 모든 감시 공간을 7로 바꾼다
def fill(board, mm, x, y):
    for i in mm : # 0,1,2 이렇게 세 방향일 수 있으므로 그중 한 방향에 대해서
        nx = x
        ny = y 
        # 일방향을 지속적으로 탐색의 경우 while문 안에 dx, dy를 더해주는 구문을 더해야 한다 
        while True:
            nx += dx[i]
            ny += dy[i]
            # 범위를 나갈 경우에도 break
            if nx< 0 or ny <0 or nx > n-1 or ny > m-1 :
                break
            # 벽을 발견할 경우에도 break
            if board[nx][ny] == 6:
                break
            # 빈 공간 발견하 7로 칠한다
            if board[nx][ny] == 0:
                board[nx][ny] = 7
# dfs 시뮬레이션을 진행한다 연산자 끼워넣기 처럼 dfs 시뮬레이션은 결과값을 global value를 통해 저장한다
# depth란 cctv count와 동일 모든 cctv 감시를 끝냈다면
def dfs(depth, arr):
    global min_value
    if depth == len(cctv):
        count = 0
        for i in range (n):
            count += arr[i].count(0)
        min_value = min (min_value, count)
        return # 함수 끝낼꺼니까
    # 재귀적으로 def를 하기 위해서는 graph에 deepcopy를 해야한다
    # 이 아이디어도 좋네 우리는 cctv 리스트 인덱스 별로 순차적으로 탐색을 진행하고 있는 것
    # 현재 감시할 cctv는 depth를 통해 확인할 수 있다
    temp = deepcopy(arr)
    cctv_num, x, y = cctv[depth]   
    # cctv를 골랐으면 여러 모드들에서 dfs를 진행해야 한다
    # 내가 했던 고민이 여기 해결되어있네 fill에 전부 temp가 쓰이는데 앞 dfs에서 temp가 바뀐다면??
    # 이를 막기위해 dfs를 돌리고 다음 for문을 가기전 deepcopy를 해야 한다
    for i in mode[cctv_num]:
        # fill만 하는게 아니라 바뀐 temp에 다음 dfs를 적용해야한다, 이때 fill을 한 순간 depth가 1증가한 것
        fill(temp, i, x, y)
        dfs(depth +1,temp )
        # 다음 for문을 돌리기전 temp를 다시 초기화 시켜야한다
        temp= deepcopy(arr)

min_value = int(1e9)
dfs(0, graph)
print(min_value)