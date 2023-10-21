'''
이모티콘 플러스 가입자수 최대가 우선 목표 그 후 이모티콘 판매액 최대로 늘리기
 n명의 사용자에게 이모티콘 m개 할인판매, 이모티콘마다 할인율 다를 수 있다 (10, 20, 30, 40)
 이모티콘 구매 비용 합이 일정가격 이상이되면 이모티콘 플러스에 가입
 1. 구매가격순으로 정렬한다면
 # 전부 40을 적용 시킨 이모티콘에서 판매금액을 늘리려면 
[[40,2900],[40,3100],[11,5200],[5,5900],[32,6900],[27,9200],[23,10000]]
먼저 이모티콘 플러스 가입자수가 최대일때 최고 높은 할인율을 구한다

'''
from itertools import product
def solution(users, emoticons):
    
    ratio = [10, 20, 30, 40] 
    max_plus = -1e9
    max_buy = -1e9
    
    for cand in product(ratio, repeat = len(emoticons)):
        plus_cand = 0
        buy_cand = 0
        for user in users:
            canbuy = 0
            ratio_st = user[0]
            buy_st = user[1]
            for i in range (len(emoticons)):
                if cand[i] >= ratio_st:
                    canbuy += int (emoticons[i] * (100 - cand[i]) * 0.01)
                    if canbuy >= buy_st:
                        plus_cand += 1
                        break
        
        # 플러스 후보에 가입되지 않았을 때 구매금액이 추가된다
            else:
                buy_cand += canbuy
        # 구매금액 갱신될 때
        if plus_cand >= max_plus:
            if plus_cand > max_plus:
                max_plus = plus_cand
                max_buy = buy_cand
            else:
                if buy_cand > max_buy:
                    max_buy = buy_cand
    return [max_plus, max_buy]