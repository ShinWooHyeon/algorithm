'''
t 에서 p와 길이가 같은 부분문자열 중 부분분자열이 나타내는 수가 p보다 작은것이 나오는
수를 return 
1.문자열에서 p[0] 보다 작거나 같은 인덱스들을 전부 고르는데
2. 인덱스 +p의 길이- 1이 t의 길이보다 작아야 한다
4. p의 길이가 1인 경우 고른 인덱스 길이 전부 answer
5. p의 길이가 1이 아닌경우 작은 애들은 전부 count, 
6. 같은 애들의 경우에만  p[1:] >= t[idx +1 : idx +len(p) -1] 인 경우만 count
'''

def solution(t, p):
    answer = 0
    base = int(p[0])
    if len(p) == 1:
        for i in range (len(t) - len(p) + 1):
            if int(t[i]) <= base:
                answer += 1
    else:
        for i in range (len(t) - len(p) + 1):
            if int(t[i]) < base:
                answer += 1
            elif int(t[i]) == base:
                if int(p[1:]) >= int(t[i+1 : i + len(p)]):
                    answer += 1
    
                
    return answer