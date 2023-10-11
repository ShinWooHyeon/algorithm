# 지도의 크기를 입력 받는다
# 밑면을 갱신하는 것
# 회전시켰을 때 리스트를 바꾸고 윗면을 출력하는 것 
# 이중 리스트로 문제를 해결하고자 한다
import sys
input =sys.stdin.readline
n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range (n)]
orders = list(map(int, input().split()))
# 앞부터 [[윗면, 밑면], [서쪽 옆면, 동쪽 옆면], [앞면, 뒷면]]의 
dice = [[0,0],[0,0],[0,0]]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for order in orders:
    nx = x + dx[order]
    ny = y + dy[order]
    # 밖으로 나갈 경우 그냥 for문 돌아가지 않는다
    if 0<= nx < n and  0 <= ny < m :
        x = nx
        y = ny
        # 주사위 4가지 방향에 따라 굴리는 방식 
        if order == 1 :
            # 윗밑면과 옆면을 서로 바꾸고 옆면의 순서를 바꿔야 한다 
            dice[0], dice[1] = dice[1], dice[0]
            dice[1][0] , dice[1][1] = dice[1][1], dice[1][0]
        elif order ==2:
            # 윗밑면과 옆면을 서로 바꾸고 윗밑면의 순서를 바꿔야 한다
            dice[0], dice[1] = dice[1], dice[0]
            dice[0][0] , dice[0][1] = dice[0][1], dice[0][0]      
        elif order == 3:
            # 윗밑면과 앞뒷면을 서로 바꾸고 앞뒷면의 순서를 서로 바꿔야 한다
            dice[0] ,dice[2] = dice[2], dice[0]
            dice[2][0], dice[2][1] = dice[2][1], dice[2][0]
        else:
            # 윗밑면과 앞뒷면을 서로 바꾸고 윗밑면의 순서를 서로 바꿔야 한다
            dice[0] ,dice[2] = dice[2], dice[0]
            dice[0][0] , dice[0][1] = dice[0][1], dice[0][0]  
        
        # 현재 주사위가 굴려져서 이동한 상태이고 이제 비교를 통해서 값을 갱신하고, 윗면을 출력해야 한다
        if graph[x][y] == 0 :
            graph[x][y] = dice[0][1]
        else:
            dice[0][1] = graph[x][y]
            graph[x][y] = 0

        print (dice[0][0])
