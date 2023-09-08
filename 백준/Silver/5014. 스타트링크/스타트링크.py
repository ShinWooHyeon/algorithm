# F층 건물 G층에 스타트링크 , 강호의 위치는 S층 , G층으로 이동원한다
# 엘리베이터에는 U버튼 D버튼 뿐이다 U층위 또는 D층아래에 해당하는 층이 없을 경우 움직이지 않는다  (초과를 의미)
from collections import deque
f, s, g, u, d= map(int, input().split())

button=[1e9] * (f+1)
move=[u, -d]

def bfs(s):
    button[s] = 0
    q=deque([s])
    while q: 
        now = q.popleft()
        for i in range (2):
            next = now + move[i]
            if  1 <= next <= f and button[next] > button[now] + 1:
                button[next] = button[now] + 1
                q.append(next) 
bfs(s)
if button[g] != 1e9:
    print(button[g])
else:
    print('use the stairs')