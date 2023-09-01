# 내 논리의 문제는 설치할 때 판단해서 매우 복잡했다
# 설치한 후 문제가 된다면 그 연산을 실행하지 않는 것이 훨씬 현명한 로직!!
# 구조물이 정상인지 확인 하는 함수 , 시간이 넉넉하기 때문에 설치한 이후때마다 확인
def possible (answer) :
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥확인
            # 바닥이거나 아래에 기둥이 있거나 양옆에 
            if y == 0  or [x, y-1, 0] in answer or  [x, y, 1] in answer  or [x-1, y, 1] in answer :
                continue # 확인한 기둥이 정상이면 바로 다음 for문 진입
            return False # continue로 탈출 못 했으면 구조가 비정상이라는 뜻이다   
        elif stuff == 1: # 보를 확인한다
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or (([x-1, y, 1] in answer) and ([x+1, y, 1] in answer)):
                continue
            return False
    # for문을 정상적으로 탈출했다면 구조물이 정상이므로
    return True
    
def solution(n, build_frame):
    answer = []
    for i in build_frame:
        x, y, a, b = i
        if b == 1:
            answer.append([x, y, a])
            if not possible(answer) :
                answer.remove([x, y, a])
        if b == 0:
            answer.remove([x, y, a])
            if not possible(answer) == True:
                answer.append([x, y, a])
    
    return sorted(answer)