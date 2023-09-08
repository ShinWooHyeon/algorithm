def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        # 시뮬레이션을 for문으로 깔끔하게 세울 수 있다 
        # 징검다리 돌들 중
        for t in temp:
            # 사람수가 더 크면 cnt를 증가시킨다
            if t - mid <= 0:
                cnt += 1
            # 그 다음돌이 더 크다면 cnt를 0으로 초기화시킨다 (이돌까지는 건널 수 있다고 판단할 수 있기 때문)
            else:
                cnt = 0
            # cnt를 증가시켰는데 k보다 크다면  for문을 중단시킨다 
            if cnt >= k:
                break
        # k보다 큰 경우는 불가능한 경우이므로 친구수를 줄여야하기 때문에 오른쪽 right 값을 mid -1로 변경한다 
        if cnt >= k:
            right = mid - 1
        # k 보다 작은 경우는 성공한 경우인데 더 많이 될 수 도 있으므로 left를 mid +1로 변경한다 
        else:
            left = mid + 1
    # 최솟값을 도출할때는 left를 출력하는구나   
    return left