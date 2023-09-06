# 균형잡힌 괄호열까지의 인덱스
def balanced_index(p):
    count = 0
    for i in range (len(p)):
        if p[i]== '(':
            count += 1
        else:
            count -= 1
        if count ==0:
            return i
# 올바른 괄호열의 판단
def check_right(p):
    count = 0
    for i in p:
        if i == '(':
            count +=1
        else: # count를 계산 하기전 닫았는데 count가 0이라면 이미 닫혀있다는 것  
            if count ==0:
                return False
            count -=1
    return True


def solution(p):
    answer=''
    if p =='': #더이상 분리할 수 없다면
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1 :]
    if check_right(u):
        answer = u  + solution(v) 
    else:
        answer='('
        answer += solution(v)
        answer +=')'
        for i in range (1, len(u)-1):
            if u[i]=='(':
                answer +=')'
            else:
                answer +='('
    
    return answer