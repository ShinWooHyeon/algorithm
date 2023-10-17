def solution(sequence, k):
    n = len(sequence)
    interval_sum = 0
    end = 0
    answer=[0, len(sequence)]
    for start in range(n):
        # end를 가능한 이동시키기 오른쪽으로
        while interval_sum <k and end < n:
            interval_sum += sequence[end]
            end += 1
        if interval_sum == k:
            if (end-1-start) < answer[1] - answer[0]:
                answer= [start, end-1]
        
        # while문이 다 돌았는데 멈춘거면 부분합이 크거나 같은 것이다 \
        # 클 경우는 end를 -1해야하고 
        
        # start가 다음칸으로 가므로 부분합에서 start 제거한다
        # 빼다가 부분합이 k보다 작아질경우 다시 end를 증가시킨다
        interval_sum -= sequence[start]
    return answer
            