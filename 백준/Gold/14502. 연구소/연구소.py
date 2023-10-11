# itertools를 사용하지 않고 조합으로 찾아보자
# 벽 설치하고 퍼져야한다
# 일단 맵을 입력받고 ,벽을 설치할 수 있는 경우들에 대해서 deepcopy 한 후 설치해서 
from copy import deepcopy
from collections import deque
n, m = map(int, input().split())
# 그래프를 입력 받으면서 조합할 빈칸들의 리스트를 만들어야 한다 
virus_map = []
blank_point = []
virus_point = []
# bfs를 할때 사용할 방향을 지정해준다
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range (n):
    line = list(map(int, input().split()))
    virus_map.append(line)
    for j in range (m):
        if line[j] == 0:
            blank_point.append((i, j))
        if line[j] == 2:
            virus_point.append((i, j))
def comb (array, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(array)):
        elem = array[i]
        for j in comb(array[ :i] + array[i + 1 :], n - 1) :
            result.append([elem] + j)  
    return result
# 조합 함수를 선언하고 설치가능한 벽의 경우들을 후보리스트로 만든다
cands = comb(blank_point, 3)


# bfs를 통해 바이러스를 확장시킨다 이때 각 후보들의 경우에 대해서 virusmap이 바뀌지 않도록 deeepcopy를 이용한다

def bfs(graph):
    q= deque(virus_point)
    while q:
        x, y = q.popleft()
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))
    # bfs를 통해 바이러스로 감염시킨 후 안전구역의 값을 구한다
    safe_zone = 0
    for i in range (n):
        for j in range (m):
            if graph[i][j] == 0:
                safe_zone += 1
    # 안전구역의 값을 반환하고
    return safe_zone
answer = 0 
for cand in cands :
    copy_map = deepcopy(virus_map)
    # 벽을 세우는 과정
    for point in cand:
        a, b = point
        copy_map[a][b] = 1
    # 벽을 세운 후 그래프에 bfs를 통해 safezone을 구한다
    answer = max(answer, bfs(copy_map))

print(answer)