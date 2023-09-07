# 백준 회의실
# 항상 끝나는 시간이 가장 적은 
import heapq
N = int(input())
schedule = []
for i in range (N):
    a, b = map(int, input().split())
    heapq.heappush(schedule,(b, a))

# 끝나는 시간이 첫번 째 요소이다 현재

now = 0
cnt = 0
while schedule:
    end, start= heapq.heappop(schedule)
    if start >= now:
        cnt += 1
        now = end

print(cnt)
