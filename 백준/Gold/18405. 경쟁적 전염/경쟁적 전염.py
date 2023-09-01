# 경쟁적 전염
# 시험관 크기랑 바이러스 개수 입력받기
from collections import deque
n , k = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 시험관 입력받기
graph=[]
virus_p=[]
for i in range (n):
    line = list(map(int, input().split()))
    graph.append(line)
    # 바이러스 번호, x,y  저장한다
    for j in range (n):
        if line[j] !=0:
            virus_p.append((line[j], i, j))
s, ans_x, ans_y = map(int, input().split())
# 낮은 순서대로 해결하기 위해 큐에 입력한다 
virus_p.sort(key = lambda x : x[0])

def bfs (graph, virus_p):
    queue= deque()
    # 바이러스 번호 순서대로 큐에 삽입
    for i in virus_p:
        queue.append(i)
    if s == 0:
        return graph[ans_x-1][ans_y-1]
    
    else:
        t=0
        while queue:
            cycle = len(queue)
            for a in range (cycle):
            
                v, x, y = queue.popleft() # 바이러스번호와 좌표 정보 받기
                for i in range (4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= 0 and nx <n and ny >= 0 and ny < n :
                        if graph[nx][ny] == 0 :
                            graph[nx][ny] = v
                            queue.append((v, nx, ny))
            
            t+=1
            if t == s:
                return graph[ans_x-1][ans_y-1]
        if s > t:
            return graph[ans_x-1][ans_y-1]

print(bfs(graph, virus_p))