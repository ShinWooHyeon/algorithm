# 2차원 배열을 회전시켴서 드래곤 커브를 세대별로 만들필요가 있다 
# 튜플은 (x,y) 형태인데 리스트에서 계산할 때는 y를 앞에 x를 뒤에 해야한다 
from copy import deepcopy
def rotated(array):
    result = []
    for point in array:
        x, y = point
        result.append((-y , x))
    return result
# 드래곤 커브를 10세대 까지 그냥 만들어 버린다 
# 끝점은 0,0을 기준을 기준으로 회전시킨점이 된다 


dragon_curve_list = [[] for _ in range (11)]
dragon_curve_list[0]=([(1,0),[(0,0),(1,0)]])
dragon_curve_list[1]=([(1,-1),[(0,0),(1,0),(1,-1)]])
for i in range (2, 11):
    curve_list =deepcopy(dragon_curve_list[i-1])
    # 드래곤 커브리스트에 끝점, 튜플 리스트를 저장한다
    fisnhied_point = dragon_curve_list[i-1][0]
    fx, fy = fisnhied_point
    for j in dragon_curve_list[i-1][1]:
        cx, cy = j
        # 90도 회전하므로 , y 만큼의 차이에 -1한만큼 x값이 변한다  
        dx = (cy -fy) * -1
        dy = (cx- fx) 
        # 기준점을 잡아야 하므로 0,0을 회전시킨점을 기준점으로 해야한다
        nx = fx + dx
        ny = fy + dy 
        curve_list[1].append((nx, ny))  
        # 기준점이 되는 0,0을 회전한다면
        if cx == 0 and cy == 0:
            curve_list[0] =(nx, ny)
    # 위 for문을 통해 새로운 드래곤 커브를 만들었다
    curve_list[1] = list(set(curve_list[1]))
    dragon_curve_list[i] = curve_list


# 드래곤 커브 10개를 다 구했다 근데 튜플인데 
dragon_map = [[0]* 101 for _ in range (101) ]
n = int(input())
for _ in range (n):
    x, y, d, g  = map(int, input().split())
    rotate_count = (4 - d) % 4
    # g세대의 1번 인덱스가 g세대의 드래곤 커브 0,0이 시작점이고 d가 0인 
    origin_curve = deepcopy(dragon_curve_list[g][1])
    # 방향의 차이만큼 회전시켜야 한다
    for i in range(rotate_count):
        origin_curve = rotated(origin_curve) 

    # 이제 x,y 만큼의 차이만큼을 전부 dragon_map에 표시할 때 더해준다
    for point in origin_curve:
        ox, oy = point
        nx = ox + x
        ny = oy + y
    # 중요한건 여기서 x좌표가 실제 리스트에서는 뒤로 가야하고 y가 앞에 와야 한다는 것이다
        dragon_map[ny][nx] = 1

# 위 과정 통해서 전부 1로 바꾼다음 개수를 센다 
answer = 0
for i in range (100):
    for j in range (100):
        if dragon_map[i][j]== 1 and dragon_map[i+1][j] == 1 and dragon_map[i][j+1] == 1 and dragon_map[i+1][j+1] ==1:
            answer += 1

print(answer)