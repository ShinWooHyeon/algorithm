import sys
input=sys.stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)
while start <= end: 
    mid = (start+end) // 2
    ans = 0
    for i in tree:
        if i >= mid:
            ans += i - mid
    
    #벌목 높이를 이분탐색
    if ans >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)