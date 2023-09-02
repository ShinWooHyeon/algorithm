import sys
from collections import deque
input = sys.stdin.readline
n, l, r =map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph=[]

for i in range (n):
    graph.append(list(map(int,input().split())))
# 함수의 구성은 다음과 같다
# 가장 큰 외곽의 이동가능한지 체크하는 함수
# 국경선 여는 함수 (닫는 함수는 굳이 필요 없을듯) 
#  국경선 국가간 이동하는 함수  (인구변경)

# 위치에서 출발해서 가능한 모든 연합을 체크해야한다 # 이부분이 살짝 헷갈렸음 
def process(x, y, index):
    # 연결된 나라 정보를 담는 리스트를 생성해야한다
    united = []
    united.append((x,y))

    # 큐 자료구조 정의
    q = deque()
    q.append((x,y))
    union[x][y]= index  # 연합번호 할당
    summary = graph[x][y] # 전체 나라 인구수
    count = 1             # 나라수 세서 나중에 평균으로 분배해야하니까
    
    # BFS 
    while q:
        x, y = q.popleft()
        # 4가지 방향 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 옆에 있는 나라 확인 연합 안되어있으면
            if 0 <= nx <n and 0 <=  ny  < n and union[nx][ny] == -1 :
                # 인구 차이 조건
                if l<= abs(graph[nx][ny]-graph[x][y]) <= r :
                    # 다음 큐에 좌표 넣기
                    q.append((nx,ny))
                    # 옆 나라에도 연합번호 할당
                    union[nx][ny]= index
                    summary += graph[nx][ny] # 연합 인구수의 합 증가
                    count += 1 # 연합의 나라수 증가
                    united.append((nx,ny))
    # 아 이게 연합이 1명이어도 summary를 인구수로 나누니까 자기값이 제대로 나온다
    for i, j in united:
        graph[i][j] = summary // count
    return count # 큰 의미 없는 return
total_count = 0 # 인구이동 횟수 

while True:
    union = [[-1]* n for _ in range (n)]
    index = 0 
    for i in range (n):
        for j in range (n):
            if union[i][j] == -1 :#아직 index가 할당되어있지 않다면 즉 방문하지 않았다면 
                process(i, j, index) #
                index += 1
    # 모든 인구 이동이 끝나면 연합이 하나도 안생겨서 연합개수가 전체 나라수와 같다면
    if index == n * n:
        break
    total_count +=1

print(total_count)