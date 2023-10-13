# 봄에 양분먹고 나이 증가 하는 함수
# 여름에 양분 추가되는 함수 # heapq자료구조를 사용해야하나
# 가을에 나무 번식하는 함수
# 겨울에 지정된 칸에 양분 추가하 (이건 그냥 for문해도 될듯)
# 번식을 어떻게 포함하고 각 칸 별로 나무들은 어떻게 저장할 것인가?
# 양분 리스트와 나무 리스트를 각각 저장해야 한다 
# 아마 자기 양분을 먹으면 양분이 감소하겠지?로 일단 접근을 하자
from collections import deque
n, m, k = map(int, input().split())
# 얘만 인덱스 할때 +1해서 고려해주기
winter_add =[list(map(int, input().split())) for _ in range (n)]

# 초기 양분 5, 나무들 모을 이차원 배열과, 죽은 나무들 모을 이차원 배열을 만든다
land = [[5] * (n+1) for _ in range (n +1)]
tree_own =[[deque()for _ in range (n + 1)] for t in range (n +1)]
dead_tree=[[[]for _ in range (n + 1)] for t in range (n + 1)]

dx = [1, 1, 1 , 0, 0 , -1, -1, -1]
dy = [1, 0, -1, 1, -1 , 1, 0, -1]

for _ in range (m):
    x, y, z = map(int, input().split())
    tree_own[x][y].append(z)

# 처음에 정렬해도 나무가 새로 심기면 정렬이 안되므로 heap 자료구조를 사용하긴 해야하는데 
dead =[]
def spring_summer(x, y):

    # x,y 칸에 있는 모든 나무들에 대해서 순차적으로 양분을 먹는다 
    # 이 과정은 처음 꺼낸 tree_own의 길이만큼 진행되어야 한다

    # aged를 만드는게 아니라 인덱스를 이용해서 그냥 바로 더해줘야지 시간초과가 안날 것이다 
    for k in range (len(tree_own[x][y])):
        # 정렬은 새로 들어오는 나무들이 appendleft를 하면 자연스럽게 될것이다 !즉 정렬되어 있다고 가정하고 해결한다면
        # 특정지점에서 양분보다 트리가 크면, k 다음부터는 전부 고려하지 않아도 된다 
        if land[x][y] < tree_own[x][y][k] :
            for i in range (k, len(tree_own[x][y])):
                dead_tree[x][y].append(tree_own[x][y].pop())
            break
        # 나이가 양분보다 크다면 나이를 먹이고 land를 감소시킨다
        else:
            land[x][y] -= tree_own[x][y][k]
            tree_own[x][y][k] += 1

    # aging 된 나무들을 다시 할당한다, 이과정도 deque로 생략 가능
    # tree_own[x][y] = aged
    
    # 이제 생긴 죽은 나무들에 대해서 양분을 증가시킨다
    for _ in range (len(dead_tree[x][y])):
        land[x][y] += (dead_tree[x][y].pop())//2
# 이 과정을 통해서 treeown과 land가 변화한 상태이다 이제 나무를 번식해야 한다
def fall_extend(x, y):
    # x,y에 있는 모든 나무들에 대해서 5의 배수라면 번식을 한다 
    for tree in tree_own[x][y]:
        if tree % 5 ==0 :
            for i in range (8):
                nx = x  + dx[i]
                ny = y  + dy[i]
                # age가 1인 나무를 번식하므로 1을 nx, ny에 붙여준다
                if 1<= nx <= n and 1<= ny <= n :  
                    tree_own[nx][ny].appendleft(1)  
def winter(winter_add):
    for i in range (n):
        for j in range (n):
            land[i + 1][j + 1] += winter_add[i][j]

# 위 4가지 함수를 다 쓰면 1년이 지난다
for h in range (k):
    for i in range (1, n+1):
        for j in range (1, n + 1):
            spring_summer(i, j)
    for i in range (1, n+1):
        for j in range (1, n + 1):
           fall_extend(i, j) 
    winter(winter_add)
# 위 과정을 거치고 treeown에 있는 tree 수를 세야 한다 길이로 세면 손쉽게 구할 수 있다
answer = 0

for i in range (1, n+1):
    for j in range (1, n+1):
        answer += len(tree_own[i][j])
print(answer)
'''
[[[], [], [], [], [], []], 
[[], [1], [1], [], [], []], 
[[], [5, 1], [1, 1], [], [], []], 
[[], [5, 1], [1, 1], [], [], []],
[[], [1], [1], [], [], []],

'''