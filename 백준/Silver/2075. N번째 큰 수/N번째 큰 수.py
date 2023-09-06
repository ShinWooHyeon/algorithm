# n개로 유지하면 끝까지 돌리고 가장 작은 값이 n번째 큰수이다
import heapq 
import sys
input = sys.stdin.readline
n = int(input())
q = []
for _ in range (n):
    numbers= map(int, input().split())
    for number in numbers:
        if len(q) < n:  # 힙의 크기 n개로 계속 유지
            heapq.heappush(q, number)
        else:
            # q의 가장작은값보다 크면 큐에 들어갈 수 있고 없으면 들어갈 수 없다
            if q[0] < number:
                heapq.heappop(q)
                heapq.heappush(q,number)

print(q[0])