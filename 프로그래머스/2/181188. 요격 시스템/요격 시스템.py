def solution(targets):
    targets.sort(key = lambda x : (x[1],x[0]))
    answer = 0
    s, e = 0 , 0 
    # target[0] 가 미사일 보다 앞에 있으면 미사일 1개를 더 추가하고 그 위치는  새로운애의 끝
    # 겹치려면 끝보다 앞에 있어야 하므로 계속 끝에 쏜다고 생각
    for target in targets:
        if target[0] >= e : # 미사일보다 뒤에 있어야 겹치는데 안 겹친다는 소리니까
            e = target[1]
            answer +=1
            
    return answer