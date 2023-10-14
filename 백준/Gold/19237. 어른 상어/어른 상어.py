n, m, k = map(int, input().split())

# 처음상어 위치
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


shark = [[0,0] for _ in range(m)]

# 상어의 초기 방향 정해주기
directions = list(map(int, input().split()))

# 상어의 방향별 우선순위 받아오기(위 아래 왼쪽 오른쪽)
priorities = []
for i in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priorities.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상황판 그리기(상어번호, 냄새가 머무는 시간)
smell = [[[0, 0]] * n for _ in range(n)]


# 냄새 정보를 업데이트 한다
def update_smell():
    for i in range (n):
        for j in range (n):
            # 냄새가 남아 있는 경우 냄새의 남은 시간을 -1한다
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 만약 그 위치가 상어가 존재한다면 냄새를 새로 갱신한다 (이동이 끝난후 즉 이동이 시작하기 전과도 동일
            if data[i][j] != 0:
                smell[i][j] = [data[i][j], k]

# 상어의 이동 함수
def move():
    new_data = [[0] *n for _ in range (n)] # 중복될 수 있으니끼ㅏ 
    for x in range (n):
        for y in range (n):
            # 빈 공간이 아니라 상어가 존재하는 곳이라면 그 위치의 상어를 옮겨야 한다
            # 상어의 방향도 지속적으로 directions에 기록 이 센스가 좋다
            # 인덱스라 -1
            if data[x][y] != 0:
                direction = directions[data[x][y] - 1]
                found = False
                # 상어의 위치인 경우
                for idx in priorities[data[x][y] -1][direction-1]:
                    #아 우선순위 행렬에서 꺼내서 되는 애 있으면 가져가는 느낌이구나
                    nx = x + dx[idx -1]
                    ny = y + dy[idx -1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0: # 냄새가 나지 않는 곳이라면  
                            # 방향 리스트의 방향을 idx로 갱신해준다
                            directions[data[x][y] -1]  = idx
                            # 새롭게 이동했을 때 거기에 상어가 없다면
                            if new_data[nx][ny] == 0:
                                new_data[nx][ny] = data[x][y]
                            else:
                                new_data[nx][ny] = min(data[x][y] , new_data[nx][ny])
                            found = True
                            break
                if found:
                    continue # 새로운 x,y에 적용하겠따 아래는 냄새 있을 경우의 이동
                # 냄새 남아있을 경우에는
                for idx in priorities[data[x][y] -1][direction-1]:       
                    nx = x + dx[idx -1]
                    ny = y + dy[idx -1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == data[x][y] : #자신의 냄새랑 같다면
                            directions[data[x][y] -1] = idx # 방향 갱신하고
                            new_data[nx][ny] = data[x][y]
                            break
    return new_data


answer = 0
while True:
    update_smell()
    new_data = move()
    data = new_data #다음 함수에 들어갈떄 data를 갱신해야하니까
    answer += 1
    check = True
    check  = True
    for i in range (n):
        for j in range (n):
            if data[i][j] > 1 :# 0도 아니고 빈칸도 아니고 1도 아닌 상어가 있다면
                check= False
                break
        if not check:
            break
    if check :
        print(answer)
        break
    if answer >= 1000:
        print(-1)
        break
                         