# 1. 벨트 회전 
#2. 로봇 전진- 가장 먼저 벨트에 올라간 로봇부터 이동, 만약 이동할 수 없다면 가만히 있는다 
# 벨트 전진 조건 이동하려는 칸에 로봇 X, 그 칸에 내구도 1 이상 
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다
# 출력 1,2,3

# 2차원리스트 한칸씩 땡기는법:deque 이용
from collections import deque
n, k = map(int, input().split())
line2= list(map(int, input().split()))
array = []
array.append(deque(line2[:n]))
array.append(deque(line2[n:][::-1]))

robot_line=deque([False] * n)

#  1.벨트회전, 로봇의 위치도 바뀐다 
def belt_rotate(array,robot_line):
    up = array[0].pop()
    down= array[1].popleft()
    array[0].appendleft(down)
    array[1].append(up)
    robot_line.pop()
    robot_line.pop()
    robot_line.appendleft(False)
    robot_line.append(False)
# 2. 현재 로봇라인에서 
def robot_going(robot_line, array):
    # 첫번째부터 마지막 전까지 있는 애들을 움직인다, 이때 내리는 위치에 도달하면 즉시 없어지므로 움직이기 전 고려할 필요가 없다
    for i in range (n-1, 0, -1):
        if not robot_line[i] : 
            # 앞에 있는 로봇부터 옮겨야 하니까 i번에 로봇이 없고 i-1번에 로봇이 있을경우  i번 내구도감소, i번으로 로봇이 온다
            if array[0][i] > 0 and robot_line[i - 1] : #내구도 감소시키고 로봇 위치 옮긴다 
                array[0][i] -= 1
                robot_line[i] , robot_line[i -1] = robot_line[i - 1] , robot_line[i]

# 3. 로봇을 올리는 과정 (올리는 위치의 내구가 0보다 크다면)
def robot_put(robot_line, array):
    if array[0][0] > 0:
        robot_line.popleft()
        robot_line.appendleft(True)
        array[0][0] -= 1
def check(array, k):
    count = 0
    for i in range (2):
        count += array[i].count(0)
    if count >= k:
        return False
    else:
        return True

ans = 1
while True:
    belt_rotate(array,robot_line)
    robot_going(robot_line, array)
    robot_put(robot_line, array)
    if not check(array, k) :
        print(ans)
        break
    else:
        ans +=1
    