import heapq
import sys
N=int(sys.stdin.readline().strip())
numbers=[]
heap=[]
for i in range (N):
    numbers.append(int(sys.stdin.readline().strip()))
for num in numbers:
    if num!=0:
        heapq.heappush(heap,num)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
        