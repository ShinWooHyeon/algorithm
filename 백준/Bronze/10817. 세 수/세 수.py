import heapq
import sys
heap=list(map(int,sys.stdin.readline().split()))
heapq.heapify(heap)
heapq.heappop(heap)
print(heapq.heappop(heap))
