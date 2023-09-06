# 중앙값 기준 큰값들을 모아둔 big heap, 작은값들을 모아둔 small heap
# big에서 가장 작은 값 small에서 가장 큰 값 ,입력받은 값 총 3가지를 비교하면 전체의 중앙값이 된다
import sys
import heapq
input= sys.stdin.readline
def solution(data):
    # 힙 2개를 만들고 작동하도록 하는 것이 포인트
    # small heap은 minheap이 파이써 기본이므로 
    small = []
    big = []
    middle = data[0]
    result = [middle]
    
    for idx, val in enumerate(data[1:], 1):
        if val > middle:
            heapq.heappush(big, val)
        else:
            heapq.heappush(small, (-val, val))
        # 처음 middle을 0번인덱스로 넣고 짝수번인덱스일때마다가 홀수번이므로  그때마다 result에 미들을 삽입한다 
        if idx % 2 ==0: # 짝수일때는 중앙값을 더 개수가 적은 곳에 숫자를 넣어야 한다 짝수기준 왼쪽 ,오른쪽이라 생각하면 편할것
            
            if len(small) < len(big):
                heapq.heappush(small, (-middle, middle))
                middle = heapq.heappop(big)
            elif len(small) > len (big):
                heapq.heappush(big, middle)
                middle = heapq.heappop(small)[1] # 양수값을 받아야 하기 때문에 1번 인덱스
            result.append(middle)
    print(len(result))

    for i in range (len(result)):
        if i != 0 and (i + 1)% 10 == 1:
            print() #10개 출력하면 줄 띄우기
        print(result[i], end=' ')
    print() # 테스트 케이스마다 또 줄 띄워야 해서

t= int(input().rstrip())
for i in range (t):
    m= int(input().rstrip())
    data = []
    if m % 10 ==0:
        for _ in range (m//10):
            data.extend(list(map(int, input().split())))
    else:
        for _ in range(m//10 + 1):
            data.extend(list(map(int, input().split())))
    solution(data)