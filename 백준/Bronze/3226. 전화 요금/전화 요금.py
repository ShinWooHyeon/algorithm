'''
7시부터 19시까지 요금 1분에 10원
19시부터 7시까지 전화요금은 1분에 5원

'''
n = int(input())
answer =0
for _ in range (n):
    case = input().split()
    now_h , now_m = int(case[0][:2]), int(case[0][3:])
    time = int(case[1])
    # 시간
    if  now_h != 6 and now_h != 18:
        if  7<= now_h < 19:
            answer += time * 10
        else:
            answer += time * 5
    # 시간이 바뀌는 경우 현재 시간이 6시또는 18시일 경우에만 고려
    else:
        if now_h ==6:
            if now_m + time <= 60:
                answer += time* 5
            else:
                answer += (60 -now_m) * 5 + (now_m + time -60) * 10
        else:
            if now_m + time <= 60:
                answer += time* 10
            else:
                answer += (60 -now_m) * 10 + (now_m + time -60) * 5 

print(answer)