# 아이디어 회전까지도 괜찮았다 그냥 계속 연ㅅ
r, c, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range (3)]


def calculate(matrix, dir) :# 연산 함수
    new_matrix , length = [] , 0 # 연산후 반환할 새로운 행렬, 최대 행의 길이
    for row in matrix:
        num_cnt = [] # 숫자, 개수 담을 리스트
        new_row = [] # 연산후 담을 row 이걸 new_matrix에 담을것이다
        for num in set(row) :
            if num == 0: 
                continue # 0은 고려하지 않으니까
            cnt = row.count(num)
            num_cnt .append((num, cnt))
        num_cnt = sorted(num_cnt, key = lambda x: (x[1], x[0])) # 빈도 순으로 정렬
        for num, cnt in num_cnt:
            new_row += [num, cnt]
        new_matrix.append(new_row)
        length = max(length, len(new_row))

    for row in new_matrix:
        row += [0] * (length -len(row))
        if len(row) > 100:
            row = row[:100]
    # 만약에 열연산으로 들어온거면 다시 
    if dir =='C':
        return list(zip(*new_matrix))
    else:
        return new_matrix

time = 0

while True:
    if time >100:
        time = -1
        break
    # 해당하느 인덱스가 변환으로 없을 수도 있으니까
    if 0 <= r-1 <len(matrix) and 0 <= c-1 <len(matrix[0]) and matrix[r-1][c-1] == k :
        break
    # 행의 개수와 열의개수 비교
    if len(matrix) >= len(matrix[0]):
        matrix = calculate(matrix, 'R')
    else:
        matrix = calculate(list(zip(*matrix)), 'C')
    time += 1

print(time)