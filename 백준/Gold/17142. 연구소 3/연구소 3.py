# 조합 함수 정의
from collections import deque
from copy import deepcopy
def comb(array, n):
    result =[]
    if n== 0:
        return [[]]
    for i in range (len(array)):
        elem = array[i]
        for j in comb(array[i +1 :], n-1):
            result.append([elem] +j)
    return result
n, m = map(int, input().split())
graph = []
virus_point = []
blanks =0
dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]
for i in range (n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range (n):
        if line[j] == 2:
            virus_point.append((i, j))
        elif line[j] ==0:
            blanks += 1
cands = comb(virus_point, m)
# 후보군들에 대해서
# bfs는 cands에 있는 애들을 활성화 시킨후 전염시킬것이다
# bfs로 무엇을 리턴할까? 전체 퍼트린 경우 time을 리턴해서 최솟값 갱신 
# bfs로 전체 못 퍼트릴 경우? -1  아마 -1이 아니라면이라는 조건을 주면 될거같다
# visited 맵을 만들어서 비활성바이러스의 경우 2지만 not visited 이면 q에 삽입하는 과정을 거친다
def bfs(cand, blanks):
    #그냥 처음부터 빈칸이 없다면
    time = 0
    if blanks == 0:
        return time
    # 빈칸이 있다면 이동가능한 여부를 확인한다
    visited =[[-1] * n for _ in range(n)]
    q= deque()

    #
    for point in cand:
        x, y = point
        visited[x][y] = 1
        q.append((x, y))
    while q:
        # 한 사이클, 즉 큐의 길이만큼 돈 다음 빈칸이 없다면
        if blanks ==0 :
            return time
        for i in range (len(q)):
            x, y = q.popleft()
            for i in range (4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 큐에서 이동한 좌표가 범위안이며 
                if 0 <= nx < n and 0 <= ny <n :
                    # 빈칸이라면 바이러스가 퍼지고 방문처리를 해야한다 나중에 비활성이랑 구분하기 위해
                    if visited[nx][ny] == -1: #방문하지않은칸일때
                        if graph[nx][ny] == 0: #그 칸이 빈칸이라면 방문처리하고 blanks 는 감소 q에 삽입
                            visited[nx][ny] = 1
                            blanks -=1
                            q.append((nx, ny))
                        # 그칸이 바이러스칸이이라면면
                        elif graph[nx][ny] == 2: #아직 방문한 적이 없다면 비활성바이러스라는거니까
                            visited[nx][ny] = 1
                            q.append((nx, ny))
        
        # 이 사이클이 다 돌았으면 time을 1 증가시켜준다
        time += 1
        # graph에 0이 없다면 다 확산된거니까

    # while문을 다돌았는데 끝나지 않은거는 blank가 0이 아니라는 것이고 그러면 실패한거니까 -1을 반환해야 한다 
    return -1

# 조합들 중 한 조합을 골라
inf = int(1e9)
ans = inf
for cand in cands:
    result = bfs(cand, blanks)
    # result가 -1이면 실패한거니까 고려하지 않고 ans의 최솟값을 모든 조합애대해서 갱신한다 
    if result != -1:
        ans = min(ans, result)

if ans != inf:
    print(ans)
else:
    print(-1)