from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
# 바이러스 맵을 입력받고
vmap = []
virus_point= []

for i in range (N) :
    line = list(map(int, input().split()))
    vmap.append(line)
    for j in range (N):
        if line[j] != 0:
            virus_point.append((line[j], i, j))
# 작은순서대로 virus_start를 정렬한다 
virus_point.sort(key = lambda x: x[0])
# nx, ny 지정
nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]
S, X, Y = map(int, input().split())
# 큐에 초기 바이러스 순서대로 삽입해야한다 
def bfs(vmap, virus_point):
    virus_start = deque(virus_point)
    if S == 0:
        return vmap[X-1][Y-1]
    else:
        t = 0
        while virus_start:
            for i in range(len(virus_start)):
                vn, a, b = virus_start.popleft()
                for j in range (4) : 
                    na = a + nx[j]
                    nb = b + ny[j]
                    if 0 <= na  < N and 0 <= nb <N and vmap[na][nb] == 0:
                        vmap[na][nb] = vn
                        virus_start.append((vn, na, nb)) 
            t += 1
            if t == S:
                return vmap[X-1][Y-1]
        # While문을 다 돌았는데도 즉 이미 바이러스 다 퍼져서 시간 덜 되었어도 종료되면
        if t< S:
            return vmap[X-1][Y-1]

print(bfs(vmap, virus_point))
#
#def bfs_virus(start, S) :
    