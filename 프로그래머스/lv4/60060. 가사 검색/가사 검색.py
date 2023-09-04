# bisect 라이브러리를 이용하여 \
# 길이로 리스트를 먼저 나눠야 효율성이 높아질 수 있다 !! 이 포인트를 잘 생각하자
# 내 아이디어 자체는 괜찮았는데 효율성을 잘 생각해야 한다

from bisect import bisect_left, bisect_right

# left_value, right value

def count_by_range (a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index  #특정 값 사이에 개수 세는 함수

# 길이에 따른 리스트 저장하는 리스트 생성
array = [[] for _ in range (10001)] 

# 접두사가 ? 일 경우 길이에 따라 revere 한 단어를 저장하는 리스트
reversed_array = [[] for _ in range (10001)]

def solution(words, queries):
    answer = []
    for word in words : # 모든 단어를 일단 array , 뒤집어서 array에 삽입한다 ,  계수정렬 생각, 길이가 인덱스 그 자체가 된다 일단 이 아이디어 
        array[len(word)].append(word)     
        reversed_array[len(word)].append(word[::-1])         
    
    # 이진 탐색 수행 위해서는 array 정렬해야함
    for i in range(10001):
    
        array[i].sort()
        reversed_array[i]. sort()

    # 쿼리를 확인해서 개수를 센다
    for query in queries:
        if query[0] != '?' : # 접두사가 ?가 아니라면
            # 이 아이디어가 생소할듯 ?를 대체하고 개수를 세기 위헤서는 ??가 될 수 있는 사전순으로 가장 앞 단어 가장 마지막 단어를 생각한다
            # ?가 전부 a 일때 가장 앞 단어, ?가 전부 z 일때 가장 뒷 단어이다
            # 길이가 쿼리인 리스트 내에서 
            cnt = count_by_range(array[len(query)], query.replace('?','a') , query.replace('?','z'))
        else:
            cnt = count_by_range(reversed_array[len(query)], query[::-1].replace('?','a') , query[::-1].replace('?','z'))
        answer.append(cnt)
    return answer