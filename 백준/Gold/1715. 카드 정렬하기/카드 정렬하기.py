import heapq 

n = int(input())

# 힙에 초기 카드 묶음을 모두 삽입한다

heap = []
for i in range (n):
    num = int(input())
    heapq.heappush(heap, num)

result = 0 

# 힙에 원소가 1개 남을때 까지 
while len(heap) != 1:
    # 가자 작은 카드 두개의 묶음을 꺼낸다
    one = heapq.heappop(heap) #알아서 최솟값이 나옴
    two = heapq.heappop(heap) 
    # 내가 원래한풀이는 20 60 70인데 이러면 처음에 80으로 묶고 80으로 시작하는게 아니라 70에서 시작해야하는게 맞는데 잘못 실행된 
    result += one + two
    sum_value = one + two # 다시 힙에 넣을 카드 묶음
    heapq.heappush(heap, sum_value)

print(result)  # 즉 묶음이 1개면 그냥 묶을필요 없으니까 카드를 그대로 둬도 되므로 0을 출력하면 된다