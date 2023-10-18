# 세로 n, 가로 m 공의 위치 startX, startY
# 친 공이 각각의 목표로한 공에 맞을 때 까지 최소 얼마의 거리를 굴러야 하는가?
# 매 회마다 목표로 해야 하는 공의 좌표 쌍이 balls
# 벽에 부딪히고 공이 굴러간 거리의 최솟값의 제곱 
# 4가지 방향 다 뒤집는데 볼로 받는 애만 기준으로 해서 한다 

inf = int(1e9)
def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        a, b = ball
        # 위로 뒤집을때
        c1 = (startX -a)**2 + (2 * n -b - startY)**2
        
        # 아래로 뒤집을때
        c2 = (startX -a)**2 + (startY + b)**2
        
        # 오른쪽으로 뒤집을때
        c3 = (2 * m -a - startX)**2 + (startY - b) ** 2
        
        # 왼쪽으로 뒤집을때
        c4 = (startX + a) ** 2 + (startY - b) **2   
        
        if startX == a: # x 좌표가 동일할경우 c1을 y가 큰애로 c2를 y가 작은애로 보고 뒤집어서 구
            # 볼이 위에 있으면 위로 올려야한다
            if startY > b : 
                c1 = ((n - startY) + (n - b))**2
                c2 = inf
            else:
                c1 = inf
                c2 = (startY + b) ** 2
        if startY == b:
            if startX > a : 
                c3 = ((m - startX) + (m - a))**2
                c4 = inf
            else:
                c3 = inf
                c4 = (startX + a) ** 2
        answer.append(min(c1,c2,c3,c4))
    return answer