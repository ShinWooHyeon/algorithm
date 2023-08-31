import heapq

def solution(food_times, k):
    # 전체 음식을 먹는시간보다 k가 크면
    if sum(food_times)<=k:
        return -1
    
    # 시간이 작은 음식부터 빼야한다
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i],i+1))
    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간 / sumvalue에 previous가 쌓이도록 계산

    length=len(food_times) #남은 음식 개수

    # 지금까지 사용한 시간 + 우선순위 큐에서 나올 현재의 음식시간   - previous (이미 몇단계 지난 후면 실제로는 현재의 음식시간에서
    # previous가 깎여 있을 상태이니까)
    while sum_value + ((q[0][0]-previous) * length) <=k:
        now=heapq.heappop(q)[0] # 현재 남아있는 시간이 가장 짧은 애의 맨 처음 시간
        sum_value += (now -previous) * length 
        length -= 1 # 다먹은 음식은 이제 제외하고
        previous = now # 4초 6초  짜리 음식이면 4초짜리 음식을 다먹고 6초 짜리 음식을 다 먹으면 이제 이전 먹은 시간은 6초여야하니까
    
    # 이렇게 하면 q에 남은 음식이 있을텐데 번호순으로 정렬 다 돌고 처음부터 돌때 번호순으로 도니까
    result = sorted(q, key=lambda x: x[1])

    # 이제 남은 시간동안 어디에 가있을지 결정하면 된다
    # 남은 시간은 k- sum_value 이므로 해당하는 
    return result[(k-sum_value) % length][1]

