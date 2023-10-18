from collections import deque
def solution(n, m, section):
    # 처음 롤러 발견하면 페인트칠한다
    # section을 deque로 하고 popleft 하고 그 뒤에꺼 
    q = deque(section)
    answer = 1
    roll_start= q.popleft()
    while q:
        next_p = q.popleft()
        if next_p <= roll_start + m -1:
            continue
        else:
            answer += 1
            roll_start = next_p
    
    return answer