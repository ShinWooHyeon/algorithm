# 출력형식이 잘못되었습니다
# 대소문자는 구별 x
# 공백의 개수차이는 상관없으나 유무 차이는 상관이 있다 공백확인했을 때 공백 공백 공백 공백 처음에는 처음은 삽입 x , 
# 문자열의 맨앞, 맨마지막 공백은 상관 x
# 특수부호의 바로앞, 바로 뒤 공백은 상관 x , 맨 마지막에 고려
# 여는 괄호끼리는 구별 x
# 닫는 괄호끼리는 구별 x
# 쉼표와 세미콜론은 구분 x  
# 즉 다 무시 할 수 있는 것들은 제거하면서 간단화 했을 때 동일한 문자열인가를 확인해야한다 


# 1. 양쪽 공백 제거 공백유무차이는 문제가 되지만 맨앞 맨뒤는 상관이 없다 
special_case=['(' ,')', '[' ,']', '{' , '}', '.' ,',', ';', ':']
tc = int(input())

for t in range (1, tc + 1) : 
    str1 = list(input().strip().lower())
    str2 = list(input().strip().lower())
    simple_str1 = []
    simple_str2 = []
    for i in range (len(str1)):
        if str1[i] in ['(', '{', '['] :
            simple_str1.append('(')
        elif str1[i] in [')', '}', ']'] :
            simple_str1.append( ')')
        elif str1[i] in ["," , ";"] :
            simple_str1.append(',')
        elif str1[i] ==' ':
            if str1[i+1] != ' ':
                simple_str1.append(' ')
        else:
            simple_str1.append(str1[i])

    for i in range (len(str2)):
        if str2[i] in ['(', '{', '['] :
            simple_str2.append( '(')
        elif str2[i] in [')', '}', ']'] :
            simple_str2.append( ')')
        elif str2[i] in ["," , ";"] :
            simple_str2.append( ',')
        elif str2[i] ==' ':
            if str2[i+1] != ' ':
                simple_str2.append(' ')
        else:
            simple_str2.append( str2[i])
    answer1 = ''
    answer2 = ''
    str1_list = list(simple_str1)
    str2_list = list(simple_str2)
    answer1 +=str1_list[0]
    answer2 +=str2_list[0]
    for i in range (1, len(str1_list) -1):
        if str1_list[i] ==' ' :
            if (str1_list[i-1] in special_case) or (str1_list[i+1] in special_case) :
                continue
        answer1 += str1_list[i]
    for i in range (1, len(str2_list) -1):
        if str2_list[i] ==' ' :
            if (str2_list[i-1] in special_case) or (str2_list[i+1] in special_case) :
                continue
        answer2 += str2_list[i]
    answer1 +=str1_list[-1]
    answer2 +=str2_list[-1]
    if answer1 == answer2:
        print(f'Data Set {t}: equal')
    else:
        print(f'Data Set {t}: not equal')
    if t == tc:
        break
    print()

