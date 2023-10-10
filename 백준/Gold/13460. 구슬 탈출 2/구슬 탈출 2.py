# N, M을 입력받고 방향 4개를 설정하여 BFS를 진행할 것이다, 
# 이 때 파랑색공이 움직였을 떄 들어오면 움직이는 과정을 생략한다 즉 CONTINUE 쓰고 새로운 BFS
# 둘이 같은 곳에 도착한다면 이동한 거리가 더 긴애를 움직인 방향 -1을 해야한다
# 빨간공 ,파란공의 좌표를 기록할 방문리스틀 만들어야한다 .
# count를 기록해야 한다 사이클을 기록하려면 큐의 길이만큼만 for문을 돌아야 한다 
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

#파란공 빨간공의 좌표를 기록해야 한다
graph = []
for i in range (N):
    line = list(input())
    graph.append(line)
    for j in range (M):
        if line[j] == 'R':
            rx, ry = i, j
        if line[j] == 'B':
            bx, by = i, j
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs (rx, ry, bx, by):
    # 방문 리스트 기록
    visited=[(rx, ry, bx, by)]
    q = deque()
    q.append((rx, ry, bx, by))
    # 움직인 횟수 기록
    count = 0
    while q:
        for _ in range(len(q)):
            rx, ry ,bx, by = q.popleft()
            # 10회 초과시 -1
            if count > 10:
                print(-1)
                return 
            # 위 if문 통과, 즉 10회 이하로 O 도착시 카운트 출력
            if graph[rx][ry] == 'O':
                print(count)
                return
            # 4가지 방향으로 빨간구슬 파란구슬을 움직인다
            for i in range (4):
                nrx, nry, nbx, nby = rx, ry, bx, by
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if graph[nrx][nry] =='#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry] =='O':
                        break
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] =='#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] =='O':
                        break
                # 먼저 파란색 구슬이 들어가면 실패이므로 for문 처음으로
                if graph[nbx][nby] =='O':
                    continue
                # 두 위치가 같다면 움직인 ㅓ리 기준으로 더 짧은애가 자리를 갖는다
                if nrx == nbx and nry == nby :
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                # 최종적으로 움직이는 동작을 전부 완료했고 이 작업 후 두 구슬의 좌표가 방문하지 않았다면 방문처리하고 큐에 삽입한다
                if (nrx, nry, nbx, nby) not in visited:
                    visited.append((nrx, nry, nbx, nby))
                    q.append((nrx, nry, nbx, nby))
        count+=1 
    # 무조건 실패하는 경우  
    print(-1)
    return
bfs (rx, ry, bx, by)