# 조합이용한 논리까지도 좋았다
from itertools import combinations

n , m = map(int, input().split())
# 치킨 리스트, 집 리스트 만드는것도 잘 했다
chicken, house = [], []

for r in range (n):
    # 현재 그래프 입력받는다
    # r이 현재 행이므로 시간 단축  가능하다 ! 이 표현도 좋다
    data= list(map(int, input().split()))
    for c in range(n):  # 여기서 c가 열번호가 된다
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

# 여기가 다른데 모든 치킨집 중 m개의 치킨집을 뽑는 조합 계산 아니 똑같은건가

chicken_new=list(combinations(chicken,m))


# 새롭게 뽑은 치킨집들의 조합에서  거리의 합을 계산 하는 함수
# 
def get_sum (chicken_new):
    result = 0 # 갱신가능한 거리 변수 생성
    # 모든 집에 대하여 좌표를 받고
    for hx , hy in house:
        temp= 1e9
        for cx, cy in chicken_new: # 절댓값 함수 그냥 쓰면 되는데 치킨집까지의 거리중에서 가장 작은값 갖고
            temp = min (temp, abs(cx-hx) + abs(cy-hy))
        result+=temp # 
    return result
# 정의한 함수를 후보군 전부를 돌려서 가장 작은값을 찾는다
chicken_length=int(1e9)
for i in chicken_new:
    chicken_length=min(chicken_length, get_sum(i))

print(chicken_length)
