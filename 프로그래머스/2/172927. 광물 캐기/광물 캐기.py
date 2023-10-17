import math
def solution(picks, minerals):
    # 파야하는 광물에서 돌일경우 우선순위 돌 -> 철 -t> 다
    # 철일경우 우선순위 철 ->
    # 다이아일경우 다 -철-돌 / 철일경우 철- 다- 돌/ 돌일경우 돌-철-다
    five_cnt = math.ceil(len(minerals)/5) 
    answer = 0
    five_can = min(sum(picks), five_cnt)
    mineral_cnt = []
    for i in range(five_can -1 ):
        dia = minerals[5 * i: 5 *(i+1)].count('diamond')
        iron= minerals[5 * i: 5 *(i+1)].count('iron')
        stone = minerals[5 * i: 5 *(i+1)].count('stone')
        mineral_cnt.append([dia, iron, stone])
    # 마지막 묶음은 (five_cnt -1) * 5 인덱스부터 곡괭이가 부족다면 끝까지, 아니라면 
    # 묶음 가능한 것보다 곡괭이수가 더 적다면 5의 배수 형태로 마지막 꺼를 붙여주고
    if sum(picks) <= five_can:
        dia = minerals[(five_can-1) *5 : five_can * 5].count('diamond')
        iron = minerals[(five_can-1) *5 : five_can * 5].count('iron')
        stone = minerals[(five_can-1) *5 : five_can * 5].count('stone')        
        mineral_cnt.append([dia, iron, stone])
    else:
        dia = minerals[(five_can-1) *5 :].count('diamond')
        iron = minerals[(five_can-1) *5 :].count('iron')
        stone = minerals[(five_can-1) *5 :].count('stone')
        mineral_cnt.append([dia, iron, stone])
    mineral_cnt.sort(key = lambda x: (-x[0], -x[1], -x[2]))
    for i in range (five_can):
        if picks[0] >0:
            picks[0] -= 1
            answer += sum(mineral_cnt[i])
        elif picks[1] >0:
            picks[1] -= 1
            answer += (5 *mineral_cnt[i][0] + mineral_cnt[i][1] + mineral_cnt[i][2])
        elif picks[2] >0:
            picks[2] -= 1
            answer += (25 *mineral_cnt[i][0] + 5 * mineral_cnt[i][1] + mineral_cnt[i][2])
    return answer