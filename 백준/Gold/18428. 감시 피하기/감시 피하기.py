# 감시피하기
import sys
from itertools import combinations
import copy
input = sys.stdin.readline
n= int(input())
graph=[]
t_point=[]
x_point =[]
for i in range (n):
    line= list(input().split())
    for j in range (n):
        if line[j] == 'T':
            t_point.append((i, j))
        elif line[j]=='X':
            x_point.append((i,j))
    graph.append(line)
candidate=list(combinations(x_point,3))

#특정방향으로 감시진행 (학생 발견시 True, 학생 미발견시 False)
def watch(x, y ,direction) :
    # 왼쪽
    if  direction ==0:    
        while y>=0:
            if graph[x][y] =='S':
                return True
            if graph[x][y] =='O':
                return False
            y-=1
    # 오른 쪽
    if  direction ==1:    
        while y<n:
            if graph[x][y] =='S':
                return True
            if graph[x][y] =='O':
                return False
            y+=1
    if  direction == 2:    
        while x>=0:
            if graph[x][y] =='S':
                return True
            if graph[x][y] =='O':
                return False
            x-=1
    if  direction ==3:    
        while x < n:
            if graph[x][y] =='S':
                return True
            if graph[x][y] =='O':
                return False
            x+=1
    # 4방향 모두에서도 발견 못 했음으로
    return False

# 선생님들이 있는 모든 위치에서 학생들 찾는 함수

def process():
    for x, y in t_point:
        # 선생위치 하나당 4가지 방향에서 확인
        for i in range(4):
            # 한방향에서라도 발견했으면 True
            if watch(x,y,i):
                return True
    # 모든 선생의 4가지 방향에서 발견 못했으면
    return False
find= False # 발견여부
for data in candidate:
    for x,y in data:
        graph[x][y] = 'O' #장애물 설치
    if not process() : # True가 발견한것이므로 후보군중 1군데에서라도 발견못했으면  다른 곳 확인안해도 괜찮다
        find= True #다 숨는 경우 찾았으므로
        break 
    # 설치 후 원상 복구
    for x,y in data:
        graph[x][y]='X'
if find:
    print('YES')
else:
    print('NO')