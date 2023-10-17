import math
def solution(r1, r2):
    # 2 x*2 = r*2 해서 x에 int해서 가장 가까운 int 구하고 
    # (1~ int -1 까지 개수 +1) * 8 
    # x축 y축 개수는 1개 구해서 * 4
    answer = 0
    answer += (r2 - r1 + 1) * 4
    mid = int(((r2 **2)/2)** (1/2)) 
    graph_yx = 0
    for i in range (1, mid + 1) :
        if i<= r1:
            a = math.ceil((r1**2 - i **2)**(1/2))
        else:
            a = 1
        if a <= i :
            a = i + 1
            graph_yx += 1
        b = math.floor((r2**2 - i **2)**(1/2))
        answer += (b - a + 1) * 8
    answer += 4 * graph_yx
    return answer
    