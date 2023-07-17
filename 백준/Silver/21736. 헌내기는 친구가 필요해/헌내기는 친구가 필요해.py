import sys; input = sys.stdin.readline
from collections import deque

dx, dy = [1,-1,0,0], [0,0,1,-1]
def near(x, y): #다음 탐색 대상을 1차 선별
    neigh = []
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < N and 0 <= b < M: neigh.append((a,b))
    return neigh

def dfs(G, s):
    visited = [[False for _ in range(len(G[0]))] for _ in range(len(G))]
    queue = deque([s])
    ans = 0
    while queue:
        (x, y) = queue.pop()
        visited[x][y] = True
        if G[x][y] == 1: ans += 1
        for a, b in near(x,y): # 벽이거나 방문했던 곳이라면 pass
            if visited[a][b]: continue
            if G[a][b] == -1: continue
            queue.append((a,b))
            visited[a][b] = True
    return ans

def school(s):
    if s == 'O': return 0
    elif s == 'X': return -1
    elif s == 'P': return 1
    elif s == 'I': return 2

N, M = map(int,input().split())
G = [list(map(school, list(input().strip()))) for _ in range(N)]
start = False
for i in range(N):
    for j in range(M):
        if G[i][j] == 2: start = (i,j);break
    if start: break

ans = dfs(G, start)
print(ans if ans!=0 else 'TT')