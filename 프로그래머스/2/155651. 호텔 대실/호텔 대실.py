# 한번 사용한 객실 10분 청소후 사용 가능
# 예약시간이 담긴 2차원 배열 book_timw이 주어진다
# 시가문제의 경우 시간을 전부 분으로 변환시켜준다
import heapq
from collections import deque
from copy import deepcopy
def check_possible(book_time, k):
    q =[]
    if len(book_time) <= k:
        return True
    else:
        for _ in range (k):
            s, e = book_time.popleft()
            heapq.heappush(q, e)
        while book_time:
            s, e = book_time.popleft()
            time = heapq.heappop(q)
            time_ac = time + 10
            if s >= time_ac:
                heapq.heappush(q, e)
            else:
                return False
    return True
def solution(book_time):
    answer = 0
    for book in book_time:
        book[0] = int(book[0][:2]) * 60 + int(book[0][3:])
        book[1] = int(book[1][:2]) * 60 + int(book[1][3:])
    book_time = deque(sorted(book_time, key = lambda x: (x[0], x[1])))
    k = 1
    while k < len(book_time):
        check_book = deepcopy(book_time)
        if check_possible(check_book, k) :
            return k
        else:
            k += 1
    
    return k