# 모든 길에 속한 모든칸의 높이가 같거나 연속되어있는 칸의 길이 차이가 1이어야 한다
n, l = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]

# 오른쪽 함수만 적용하기 위해 회전 행렬을 정의해야한다
road_rotate =[[0] * n for _ in range (n)]
for i in range (n):
    for j in range (n):
        road_rotate[j][n-i-1] = road[i][j]

# 행을 기준으로 오른쪽으로 길 확인 하는 함수

# i번째 인덱스까지 확인 완료, i를 증가시키다가 안될 경우 return False 한다 
# 현재 상태 (경사로가 끝난 상태 0, 위로 가는 경사로 1, 아래로 가는 경사로 2)
def road_find_right(i, state, down_count):
    # n-1열 까지 다 돌았을때 문제가 없고 경사로가 끝난 상태라면 
    if i== n - 1 :
        if state == 0:
            return True
        else:
            return False
    else:
        # 경사로가 끝난상황이라면 
        if state == 0:
            # 두 길이 연속된다면  down_count 를 1 증가시킨다
            if line[i] == line[i+1]:
                return road_find_right(i + 1, state, down_count + 1)
            # 두 길의 길이가 다르다면 아래로 가는 경우와 위로 가는경우가 있다
            else:
                # 두 길의 차이가 1이 아니라면 false를 return한다
                if abs(line[i] - line[i + 1]) != 1:
                    return False

                else:
                # 아래로 가는 길이라면 , down_count를 1로 초기화 하고 아래로 가는 상태로 바꾼다음 return 한다 
                    if line[i] - line[i +1] == 1:
                        down_count = 1
                        # 만약 l이 1이라면 
                        if l == 1:
                            return road_find_right( i + 1, 0, 0)
                        else:
                            return road_find_right( i +1 , 1, down_count)
                    # 위로 가는 길이라면 아래로 연속된 숫자가 l개 이상이어야지 이을 수 있고 그렇지 않다면 False
                    else:
                        if down_count >= l:
                            down_count = 1
                            return road_find_right( i +1, 0, down_count)
                        else:
                            return False
        # 현재 아래로 가는 경사로 상황이라면  l이 1인 경우는 전부 바로 없어지므로 일단 고려 x ,아직 l에 모자란경우만있다
        elif state == 1:
            # 두 숫자가 같다면 연속된 숫자이므로 연결시키고 down_count를 1 증가시킨다 
            if line[i] == line[i+1]:
                down_count += 1
                # l과 같다면 down_count를 1로 초기화 시키고 0 상태로 return 한다
                if down_count == l:
                    down_count = 0
                    return road_find_right( i + 1, 0, down_count)
                # 아직 l에 모자라다면 1상태 그대로 return한다
                else:
                    return road_find_right( i + 1, 1, down_count)
            # 경사로인데 아직 l이 안되었는데 모자라다면 False를 return 한다
            else:
                return False
answer= 0
for line in road:
    # 제대로 road라면
    if road_find_right(0, 0, 1):
        #print(line)
        answer += 1
#print('---------------')
for line in road_rotate:
    if road_find_right(0, 0, 1):
        #print(line)
        answer += 1

print(answer)