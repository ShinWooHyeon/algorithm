'''
col번째 칼럼 값 기준으로 오름차순 정렬, 동일하면 첫번째 칼럼의 값을 기준으로 내림차순 정렬
정렬된 데이터에서 
'''
def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x: (x[col -1], -x[0]))
    for i in range (row_begin, row_end + 1):
        total = 0
        for j in data[i -1]:
            total += j% i
        answer ^= total
    
    return answer