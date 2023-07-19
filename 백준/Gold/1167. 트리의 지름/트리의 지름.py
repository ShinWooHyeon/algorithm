import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
visited = [False]*(n+1)
adjacent = [ [] for _ in range(n+1) ]

for i in range(1,n+1):
    req = list(map(int , input().strip().split()))
    index = 0
    S1 = req[index]
    index+=1
    while True:
        S2 = req[index]
        if S2 == -1:
            break
        E = req[index+1]
        adjacent[S1].append((S2,E))
        index+=2

distance = [0] * (n+1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start]=True
    while len(queue)!=0:
        node = queue.popleft()
        for i in adjacent[node]:
            if visited[i[0]] == False:
                queue.append(i[0])
                visited[i[0]]=True
                distance[i[0]]= distance[node]+i[1]

bfs(1)
result_index = distance.index( max(distance) )
visited = [False]*(n+1)
distance = [0] * (n+1)
bfs(result_index)
print(max(distance))