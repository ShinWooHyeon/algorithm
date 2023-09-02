# 균형잡힌 괄호 문자열의 인덱스 반환 즉 u,v를 구하기 위한 인덱스 여기까지는  해결
def balance_index(p) :
    count= 0 #왼쪽 괄호의 개수를 세야 한다
    # 반대되는개수가 같아야할 때 두 개의 합을 0으로 만드는 개념도 좋다 
    for i in range(len((p))):
        if p[i] =='(':
            count += 1
        else:
            count -= 1
        if count ==0:
            return i

# 올바른 괄호 문자열인지 판단 #이 구현을 제대로 하지 못해 풀이 실패

def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count +=1
        else: # 닫을 때 뺄셈을 해줘서 균형이 맞아야하는데 빼기도 전에 닫았는데 0이면 균형이 안맞는다는 소리 
              # 즉 닫는 괄호 앞에 왼쪽 괄호가 1개 더있었다는 말 즉 닫기가 더 많이 나와선 안된다 
            if count == 0: # 
                return False
            count -= 1
    return True


def solution (p):
    answer = ''
    if p == '':
        return answer
    index = balance_index(p)
    u = p[:index+1]
    v = p[index+1:]
    # 문제 그대로 조건을 수행한다 왼쪽 조건과 비교하면서 보자 
    if check_proper(u) :
        answer = u +solution(v)
    # 올바른 괄호 문자열이 아니라면 
    # answer에 대한 재귀를 할때 다른데서의 ans 재귀가 맨처음 시작의 ans에 영향 x
    # 맨처음 ans에는 ans 변수가 없이 ans= u+sol(v) 이므로 
        
    else:
        answer='('
        answer += solution(v)
        answer += ')'
        mid_u= u[1:-1]
        for i in mid_u:
            if i == '(':
                answer += ')' 
            else:
                answer += '('
    return answer