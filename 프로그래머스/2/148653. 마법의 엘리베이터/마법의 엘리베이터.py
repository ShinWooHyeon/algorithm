'''
0층으로 가기 위한 최소 횟수 -1, +1 , 절댓값이 10의 c 승
0층이 가장 아래층 ,
즉 자신의 수에서 10의 배수에 가장 가깝게 만들어야하는데 
자릿수를 보고 
n= len(storey) , n-1을 기준으로 어디에 더 가까운지 확인한다 더 가까운쪽을 발견하면 
n이 더가까우면 10**n - 현재수를 증가시켜야하고 n-1이 더가까우면 현재수- 10**n-1을 감소시켜야 한다
다시 그 차이에 
'''
answer = 0
def solution(storey):
    global answer
    n = len(str(storey))
    if storey ==10 ** (n -1):
        answer += 1
        return answer
    if n == 1:
        if storey > 5:
            answer += (10 - storey) + 1
        else:
            answer += storey
        return answer
    # 두 자리수 이상일 때는
    if 10**n - storey >= storey - 10** (n -1):
        answer += 1
        return solution(storey -10** (n-1))
    else:
        answer += 1
        return solution(10**n - storey)
    return answer