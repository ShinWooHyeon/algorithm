# 내가 생각한 두자리 수가 문제가 되지 않는 이유 두 자리여도 그냥 문자열 자체를 구해서 길이를 구하면 되기 떄문
# 문제를 드디어 이해했다 3개 압축이면 무조건 3개/3개/3개/3개/3개/3개 이형태에서 묶는거다!
def solution(s) :
    answer = len(s)
    for step in range(1, len(s)//2+1):
        compressed = "" #압축된 문자열
        prev= s[0:step] 
        count=1 
# 이 표현이 정말 익숙하지 않지만 잘 생각해보면 문자열 길이만큼 증가시키면 내가 생각한 계속 같은길이만큼 슬라이싱 할 필요가 없다
        for j in range (step, len(s),step) :
        # 이전 상태와 동일하다면 count 증가
            if prev == s[j:j+step] :
                count+=1
        # 중요한 포인트 count가 1이면 길이가 오히려 1  늘어남 count가 2 이상일 때만 고려
            else:
                compressed+= str(count) + prev if count >=2 else prev # 이표현을 잘 보자 count+문자열 or 문자열을 그대로 더한다는 뜻이다
                count=1
                prev=s[j:j+step]
        # 남아있는 문자열에 대해서 처리 예르들어 길이가 14 3개씩 묶었다 치면 12개 하고 2개가 남았는데 그 2개는 무조건 길이도 다르므로
        # if prev==s[j:j+step] 에서 else로와 compressed에 더해지고 남은 2개의 문자열에대해서 prev가 되서 더해질 필요가 있따
        compressed += str(count) + prev if count>=2 else prev

        # 만들어진 길이 중 계속 작은값을 기록
        answer=min(answer, len(compressed)) 

    return answer

