# 과제는 시작시간에 시작
# 과제 진행 중 새로운 과제 시간 되면 새로운 과제 시작, 진행중이던 과제 멈춘다
# 진행중이던 과제 끝냈을 때 시작해야할 과제가 없다면 멈춰둔 과제를 이어서 진행한다
# 멈춰둔 과제가 여러개일 경우 최근 과제부터 시작해야 한다 후입 선출 (그냥 리스트)
from collections import deque
def solution(plans):
    # 가장 먼저 문자열로 주어진 시간들을 전부 분단위로 바꿔준다
    for i in range (len(plans)):
        plans[i][1] = int(plans[i][1][:2]) * 60 + int(plans[i][1][3:])
        plans[i][2] = int(plans[i][2])
    # 시간순 정렬을 한다
    plan_list = deque(sorted(plans, key = lambda x : x[1]))
    # 현재시간, finished work, stop work 를 구분한다
    finished_work = []
    stop_work = []
    name, start, play = plan_list.popleft()
    current = start
    while plan_list:
        name_nx, start_nx, play_nx = plan_list.popleft()
        # 현재 시간 + 현재 하고 있는 것의 작업시간이 다음 시작시간보다 짧다면
        if current + play <= start_nx :
            # 현재 작업물은 끝나고, stopwork 가 있다면 stopwork를 처리한다
            finished_work.append(name)
            if stop_work:
                remain_time = start_nx -current - play
                while remain_time >0 and len(stop_work) > 0:
                    name_stop, play_stop = stop_work.pop()
                    if play_stop <= remain_time:
                        remain_time -= play_stop
                        finished_work.append(name_stop)
                        continue
                    else:
                        stop_work.append([name_stop, play_stop - remain_time])
                        remain_time = 0
            # stop work가 있던 없던 현재 시간은 start_nx가 된다
            current = start_nx
            play = play_nx
            name = name_nx
        # 작업도중 다음 작업이 온다면
        else:
            play_remain = current + play - start_nx
            stop_work.append([name, play_remain])
            # 뽑았던 다음 작업들이 이제 현재 작업이 된다
            current = start_nx
            play = play_nx
            name = name_nx
    # 플랜리스트의 마지막 작업은 finished work에 붙여주고 stop work가 남아있다면 reverse 해서 붙여줘야 한다
    finished_work.append(name)
    if stop_work:
        for i in range (len(stop_work) -1,-1, -1):
            finished_work.append(stop_work[i][0])
    return finished_work

