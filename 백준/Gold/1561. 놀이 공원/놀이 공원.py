# 백준 놀이공원 복습 필수
# N명의 아이. M개의 놀이기구 (1번부터 M번)
# 운행시간 지나면 탑승하던 아니 내린다 . 놀이기구 비어있으면 줄 맨앞 아이가 탑승한다 
# 놀이기구 여러개 비어있으면 더 작은 번호 놀이기구 탑승한다 
# 놀이기구 비어있는 상태에서 첫 번째 아이가 놀이기구 탑승, 마지막 아이 몇번 탈까?
# 이진탐색을 하는데 1번이 최대 돌아갈 수 있는 시간 기준으로 체크한다
n, m = map(int, input().split())
times = list(map(int, input().split()))
start = 0
end = n * times[0]
#print(times)
# 총 사용 시간을 mid로 잡고 해결한다 
def binary_search(target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    clear =  0 # 시간까지 탑승했고 탑승 완료한 사람의 합 
    can_ride = 0
    ride_num=[]
    #print(f'mid값은 {mid}')
    for i in range (len(times)):  
        time = times[i]
        if mid % time !=0:
            #print(f'clear에 {mid//time + 1} 을 더했습니다')
            clear += (mid//time) + 1
        else:
            #print(f'clear에 {mid//time } 을 더했습니다')
            clear += (mid//time)
            ride_num.append(i)
            can_ride += 1
    #print(f'mid값은 {mid}, clear 값은 {clear}')
    if clear >=n:
        return binary_search(target, start, mid-1)
    else:
        #print(f'mid값은 {mid}, clear 값은 {clear}, can_ride는 {can_ride}, target은 {n}')
        if clear + can_ride >= target:
            return ride_num[target -clear - 1] + 1
        else:
            return binary_search(target, mid +1, end)
print(binary_search(n, start, end))