# 투포인터를 사용해서 갱신하는 법
# dfs 개념 =>
import sys
from copy import deepcopy
input = sys.stdin.readline

# 입력값을 받는다
N = int(input())
board =[list(map(int, input().split())) for _ in range (N)]

# 4가지 방향으로 움직이는 함수 
# up
def up(board):
    for j in range (N):
        pointer = 0
    # 포인터를 기준으로 생각해야 하기 때문에         
        for i in range (1, N) :
            # 현재 위치가 0이 아닌 숫자라면 움직임을 수행해야 하므로
            if board[i][j] : # 0이 아니라면
                #현재 값 tmp
                tmp = board[i][j]
                board[i][j] = 0  # 일단 움직일거니까 자기 위치 값은 0으로 어떻게든 이동할거라는 생각 
                # 포인터가 가리키는게 0이라면 
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                #포인터가 가리키는수와 자신이 같은 수라면 합쳐지고 합쳐진 수는 더이상 변화 x 고정이므로 pointer += 1
                elif board[pointer][j] == tmp :
                    board[pointer][j] += tmp
                    pointer += 1 
                # 포인터와 가리키는수와 자신이 다른 수라면 포인터 앞까지 이동하고 포인터 + 1, 자기자신이 포인터가 된ㄷ 
                else:
                    pointer += 1
                    board[pointer][j] = tmp
    return board

def down(board):
    for j in range (N):
        pointer = N -1  
    # 포인터를 기준으로 생각해야 하기 때문에         
        for i in range (N-2, -1, -1) :
            # 현재 위치가 0이 아닌 숫자라면 움직임을 수행해야 하므로
            if board[i][j] : # 0이 아니라면
                #현재 값 tmp
                tmp = board[i][j]
                board[i][j] = 0  # 일단 움직일거니까 자기 위치 값은 0으로 어떻게든 이동할거라는 생각 
                # 포인터가 가리키는게 0이라면 
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                #포인터가 가리키는수와 자신이 같은 수라면 합쳐지고 합쳐진 수는 더이상 변화 x 고정이므로 pointer += 1
                elif board[pointer][j] == tmp :
                    board[pointer][j] += tmp
                    pointer -= 1 
                # 포인터와 가리키는수와 자신이 다른 수라면 포인터 앞까지 이동하고 포인터 + 1, 자기자신이 포인터가 된ㄷ 
                else:
                    pointer -= 1
                    board[pointer][j] = tmp
    return board
# LEFT
def left(board):
    for i in range(N):
        pointer = 0
        for j in range(1, N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[i][pointer]= tmp
    return board

# RIGHT
def right(board):
    for i in range(N):
        pointer = N - 1
        for j in range(N - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = tmp
    return board

# 위 과정을 dfs로 찾고 싶으면 dfs 함수에 cnt를 기록해야 한다 이 과정 집중
def dfs(board, cnt):
    if cnt == 5:
        # 2차원 배열 요소 중 가장 큰 값을 반환한다
        return max(map(max, board))
    # 상하좌우 에서 리턴 값 중 큰값 반환
    return max(dfs(up(deepcopy(board)), cnt +1), dfs(down(deepcopy(board)), cnt +1), dfs(left(deepcopy(board)), cnt +1), dfs(right(deepcopy(board)), cnt +1))


print(dfs(board, 0))