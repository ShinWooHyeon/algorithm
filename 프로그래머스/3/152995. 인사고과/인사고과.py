# 임의의 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 있으면 인센티브 X
# 두 점수의 합 높은 순으로 인센티브 차등 지급
# 같으면 그 수만큼 다음 석차 
# scores가 주어졌을 때 완호의 석차를 return # 완호는 0번
# sort -x[0], -x[1] 하고
# 현재까지 가장 큰 x[1]을 갱신하고 x[1] 이 더크면 갱신한다 
# 인센티브 일단 
# sorted로 새
def solution(scores):
    answer = 0
    wanho = scores[0]
    scores.sort(key = lambda x: (-x[0], -x[1]))
    max_0 = scores[0][0]
    max_1 = scores[0][1]
    max_0_cand = -1e9
    max_1_cand = -1e9
    incentive = []
    # 비교는 x[0] 기준 앞 번호까지의 x[1] 값중 가장 큰 값 
    # 내 x[0]가 앞 x[0] 보다 작아졌을 때 x[1]을 갱신한다 
    # x[1]은 후보로 지속적으로 갱신하고 
    # 내가 보고 있는 위치는 
    for score in scores:
        if max_0_cand > score[0]:
            max_0 = max_0_cand
            max_1 = max_1_cand
        if score[0] < max_0 and score[1]  < max_1:
            continue
        # 현재보다 x1이 크다면 max_0 max_1을 후보로 설정하고 x[0] 값이 현재 cand보다 작아졌을 때 바꿔준다 
        if score[1] > max_1:
            max_0_cand = score[0]
            max_1_cand = score[1]
        incentive.append(score)                
    if wanho in incentive:
        incentive_rank = []
        for score in incentive :
            incentive_rank.append(sum(score))
        incentive_rank.sort(reverse = True) 
        return incentive_rank.index(sum(wanho)) + 1
    else:
        return -1