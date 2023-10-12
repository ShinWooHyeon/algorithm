n, m, h = map(int, input().split())
visited = [[False] * (n +1) for _ in range (h + 1)]
combi = []
# 나는 연결 자체를 2개 인덱스를 변환해서 풀었지만 그냥 인덱스 자체의 의미를 오른쪽과 연결되어 있다라고 생각하면 편하다
for _ in range (m) :
    a, b = map(int, input().split())
    visited[a][b] = True

# 기둥 보처럼 자기자신으로 오는지 체크해야 한다 
# 아래로 이동하는 과정을 이중 for문으로 깔끔하게 표현했다 이런걸 해야되는데 
def check():
    for i in range (1, n + 1):
        now = i
        for j in range (1, h + 1):
            # 자기 또는 자기 왼쪽에 사다리가 있는지 확인 그러면 이동여부 아니까
            if visited[j][now] :
                now += 1
            # 0번인덱스를 이미 false로 만들어 놨기 때문에 상관이 없다
            elif visited[j][now - 1]:
                now -= 1 
        if now != i:
            return False

    return True   

# answer이 변화하지 않고 4에 위치한다면 -1을 출력
def dfs(depth, idx):
    global answer
    # 이렇다면 answer은 변하지 않을 것이다
    if depth >= answer :
        return 
    # 현재 depth에서 체크했는데 자기자신으로 온다면 즉, 해결했다면
    if check():
        answer = depth
        return
    for c in range (idx, len(combi)):
        x, y = combi[c]
        # 모든 x,y 가 중복되지 않으므로 not x,y는 고려할 필요가 없다 True 할거면 해결되기 때문에
        if not visited[x][y-1] and not visited[x][y+1]:
            # x와 y에 설치했을 때 조합처럼 생각하자 모든 경우 c번인덱스를 고른 순간 앞과 c의 조합은 이미 고려했을 것이므르
            # idx에 c를 1증가시켜야 한다  
            # [1,2,3,4,5,6] 1번 방문, dfs로 다음부터는 2번부터 보는데 재귀로 4번 봤으면 이제 다시 5번부터 골라야함
            visited[x][y] = True
            dfs(depth +1, c +1)
            visited[x][y] = False

# 사다리 후보군이므로 마지막 열은 고려하지 않는다
# 설치하고 싶은 곳과 그 다음에 사다리가 없어야하고 연속되면 안되므로 설치하고 싶은 곳 앞도 없어야 한다 
# combi는 설치 가능한 후보군
# 순열을 생각하면 0 쌓고 나머지 1개씩 쌓아보면서  
for i in range (1,h + 1):
    for j in range(1, n):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j + 1] :
            combi.append((i, j))

answer = 4
dfs(0,0)
if answer <4 :
    print(answer)
else:
    print(-1)