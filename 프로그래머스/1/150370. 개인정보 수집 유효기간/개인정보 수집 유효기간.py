# 모든달은 28일 까지
# 약관마다 유효기간 있다고 가정 
# 오늘 날짜가 유효기간 지났ㅇ
def solution(today, terms, privacies):
    answer = []
    # 현재 날짜가 유효기간 지난 후 날짜보다 후면 파기
    term_dic = {}
    for term in terms:
        term_dic[term[0]] = int(term[2:])
    # 일은 +27을 28로 나눈 나머지
    # 달은 +5 + 일을 28로 나눈 몫 을 12로 나눈 몫
    # 년은 달에서 구한 몫을 더한다
    cnt = 0
    for pr in privacies:
        cnt += 1
        year = int(pr[:4])
        month = int(pr[5:7])
        day= int(pr[8:10])
        case = pr[11]
        if day != 1:
            day -=1
            month += term_dic[case]
        else:
            day = 28
            month += term_dic[case] -1

        if month % 12 != 0:
            year += month //12
            month = month% 12
        else:
            year += (month//12) -1
            month = 12

        if int(today[:4]) > year :
            answer.append(cnt)
        elif int(today[:4]) == year:
            if int(today[5:7]) > month:
                answer.append(cnt)
            elif int(today[5:7]) == month:
                if int(today[8:10]) > day:
                    answer.append(cnt)
                
            
    return answer