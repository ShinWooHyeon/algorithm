'''
첫 글자 x
x 와 x가 아닌 다른 글자 나온 횟수 섿나 같은 순간 멈추고 읽은 문자열 분리한다
분해한 문자열의 개수 

'''
def solution(s):
    answer = 0
    while s :
        x = s[0]
        x_cnt = 0
        y_cnt = 0
        if len(s) == 1:
            answer += 1
            break
        else:
            for i in range(len(s)):
                if s[i] == x:
                    x_cnt +=1
                else:
                    y_cnt += 1
                if x_cnt == y_cnt:
                    answer += 1
                    if i < len(s) -1:
                        s = s[i +1 :]
                    else:
                        s= ''
                    break
            else:
                answer += 1
                break
            
                    
                    
    return answer