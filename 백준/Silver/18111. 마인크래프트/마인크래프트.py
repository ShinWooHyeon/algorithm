import sys
input = sys.stdin.readline
n, m ,b = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range (n)]
answer = sys.maxsize

# 0층부터 256층 까지 반복한다
for height in range (257):
    large_h, small_h = 0, 0

    for i in range (n):
        for j in range (m):
            if graph[i][j] - height > 0:
                large_h += graph[i][j] -height
            else:
                small_h -= graph[i][j] - height
    # 블록뺀거 + 인벤토리가 더해야할거보다 커야지만 가능
    if large_h + b >= small_h :
        test_time = large_h * 2 + small_h
        if test_time <= answer: # 시간 같아도 갱신해야 더 높은 높이 가능
            answer = test_time
            answer_height = height

print(answer, answer_height)