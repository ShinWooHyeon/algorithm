# deque로 어떻게 칸 마다 순서대로 말들이 이어져 있는지 기록
# 리스트에 (번호, 자기 말 위치, 자기 말 수직 위치, 이동방향)를 기록한다 
# pop한 x,y가, deque에서  수직위치~ 길이까지 뽑으니까  popleft나 pop을  len - 수직위치 + 1을 한다 
# 그렇게 해서 전체 연결되어있는 애들의 각각의 수직위치를 설정 한 후 for문을 돌려서 원래 리스트를 갱신해준다
from collections import deque
n, k = map(int, input().split())
board =[list(map(int ,input().split())) for _ in range (n)]
chess =[[[] for _ in range (n) ] for _ in range (n)]
horse = []
stop = 0 
# 방향 인덱스는 -1해서 적용
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
# horse 인덱스가 말 번호 -1이다
# 말 번호 
for i in range (k):
    x, y, d = map(int, input().split())
    horse.append([x-1, y-1, d-1])
    chess[x-1][y-1].append(i)

count = 0

# 방향 바꾸는 걸 이렇게 표현할 수있구나
def change_dir(d):
    if d in [0 , 2]:
        d += 1
    elif d in [1, 3]:
        d -=1
    return d
# for문으로 인덱스 0~ k-1까지 즉 말번호를 돌려서 넣을것
def solve(h_num):
    x, y, d = horse[h_num]
    nx = x + dx[d]
    ny = y + dy[d]
    if nx <0 or nx >= n or ny <0 or ny >= n or board[nx][ny] ==2: # 방향을 바꾸고 이동해야한다
        d= change_dir(d)
        # 방향 바꾼 다음 새로운 nx, ny 지정
        horse[h_num][2] = d
        nx = x + dx[d]
        ny = y + dy[d]
        if nx <0 or nx >= n or ny <0 or ny >= n or board[nx][ny] ==2:
            return True # 얘도 못 움직이면 아무런 변화가 없는거 니까 그냥 아래 움직이는 과정 하지 않고 return True
    # 두 번째 위 if문 안거쳤다면 nx, ny가 바뀐채로 이동가능한거니까 아래 똑같이 적용
    horse_up = []
    # 높이를 지정해줄 필요 없이 enumerate로 그때그떄 알아서 리스트 idx 순서로 가져가도록 한다
    # x,y에 있는애 다 움직여야 하니까 그 중 자기 번호 찾았을 때 위부터 옮긴다
    for h_idx, h_n in enumerate(chess[x][y]) :
        if h_n == h_num:
            horse_up.extend(chess[x][y][h_idx:])
            chess[x][y] = chess[x][y][:h_idx]
            break
    # 옮기는 리스트 만큼 잘라서 , 빨강색이라면 그대로 위에 붙인다 (흰색 빨강색 과정은 동일 붙이는게 다를 뿐)
    if board[nx][ny] == 1:
        horse_up = horse_up[::-1]
    
    # 옮기는 말들에 대해서 # horse는 h가 말 번호고 0번이 x , 1번이 y 말 옮겨서 갱신해주고 
    for h in horse_up:
        horse[h][0], horse[h][1] = nx, ny
        chess[nx][ny].append(h) # 수직으로 쌓는다 nx, ny에
    
    if len(chess[nx][ny]) >= 4:
        return False
    # 위 과정 다 거쳐도 문제 없으면
    return True

while True:
    what = False
    if count > 1000:
        print(-1)
        break
    for i in range (k):
        # 말을 옮겼는데 4개 이상이 되었다면
        if solve(i) == False:
            what = True
            break
    count += 1
    # 쌓았으면
    if what :
        print(count)
        break