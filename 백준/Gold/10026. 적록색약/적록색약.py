import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        dxdy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if -1 < nx < n and -1 < ny < n:
                if grid[nx][ny] == grid[x][y] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

n = int(input())
grid = [list(map(str, input().strip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

ncw = 0 #색약 x
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            ncw += 1
print(ncw, end=' ')

cw = 0 #색약
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cw += 1
print(cw)