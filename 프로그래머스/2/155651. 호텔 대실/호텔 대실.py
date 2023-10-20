# 한번 사용한 객실 10분 청소후 사용 가능
# 예약시간이 담긴 2차원 배열 book_timw이 주어진다
# 시가문제의 경우 시간을 전부 분으로 변환시켜준다
import heapq
from collections import deque

def solution(book_time):
    answer = 0
    for book in book_time:
        book[0] = int(book[0][:2]) * 60 + int(book[0][3:])
        book[1] = int(book[1][:2]) * 60 + int(book[1][3:])
    book_time = deque(sorted(book_time, key = lambda x: (x[0], x[1])))
    q =[]
    answer = 1
    start, end = book_time.popleft()
    heapq.heappush(q,end)
    while book_time:
        s, e = book_time.popleft()
        end = heapq.heappop(q)
        if s >= end + 10: # 이 s 기준으로다 q에 집어넣어 준다 다시'
            heapq.heappush(q, e)
        else:
            answer += 1
            heapq.heappush(q,end)
            heapq.heappush(q,  e)

    return answer
