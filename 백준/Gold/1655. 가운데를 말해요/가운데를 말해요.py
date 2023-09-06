# 백준 가운데를 말해요 # 내 로직은 좋았는데 코드가 아쉬웠나
import heapq
import sys

n = int(sys.stdin.readline())

leftHeap = []
rightHeap = []
for i in range(n):
    num = int(sys.stdin.readline())
    # 길이가 같다면 무조건 leftheap에 넣은다음 어차피 5개니까 가장 작은값이 중앙값이 된다 
    # 왜나면 중앙값중 작은수를 결국 출력해야 하기 때문 다르면 right힙의 개수가 부족할 것이기 때문에 
    # 이렇게 넣은다음 left heap 최대 right heap  최소를 비교해서 크기가 교차된다면 서로 바꿔준다
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)
    
    print(-leftHeap[0])