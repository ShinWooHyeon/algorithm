# 계수정렬을 쓸지 그냥 정렬을 쓸지 가 일단 고민
# 정렬 한 후에  [1 2 2 2 3 3 4 6]
# 개수 세는 리스트 생성해서 세고
# 실패율 리스트 만드어서 
# 모든 스테이지마다 실패율 계산해서 
# N +1이 스테이지에 있을 경우 깬 사람 수 
def solution(N, stages):
    answer=[]
    length = len(stages) # 남아 있는 사람수 , 후에 0이면 모든 스테이지 실패율이 0으로 계산
    
    # 스테이지 번호를 1부터 N 까지 증가시키며
    for i in range (1, N+1):
        # 단순히 카운트 함수를 쓴다?
        count = stages.count(i)
        # 실패율을 계산한다
        if length == 0:
            fail = 0
        else:
            fail = count /length
        answer.append((fail, i))
        length -= count
    answer.sort(key = lambda x: -1* x[0]) # 이미 그 다음 요소를 기준으로 오름차순 정렬이 기본
    answer = [i[1] for i in answer]
    return answer