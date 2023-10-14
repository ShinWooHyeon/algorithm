# 원판 회전시킬 거니까 deque로 받는다

from collections import deque
n, m, t = map(int, input().split())
circles= [deque(list(map(int ,input().split()))) for _ in range (n)]

# 원판번호, 방향, k
def rotate(x, d, k):
    if d == 0:
        cd = 1
    elif d==1:
        cd = -1
    # 회전시키고 인접한애들을 삭제해야 한다 
    # 배수인 애들을 동시에 다 회전시켜야 한다  n 까지 x의 모든 배숫들에서  -1해야 인덱스 해서 전부 회전시킨 후  
    for i in range (x, n+1, x):
        mx = i
        for _ in range (k):
            circles[mx-1].rotate(cd)
    check_same = []
    # 같은 원판내에서 인접한 것을 체크 한다  False로 둘거니까 False는 고려하면 안된다
    for i in range(n):
        for j in range (m-1, -1, -1):
            if circles[i][j] != False:
                if  circles[i][j] == circles[i][j-1]:
                    check_same.append((0, i, j))
    
    # 다른 원판 끼리 인접한  것을 체크한다 열이 같아야한다 
    for j in range (m):  
        for i in range (n-1): # 마지막 원판은 다음 원판이 없으니까
            if circles[i][j] != False:
                if circles[i][j] == circles[i +1][j]:
                    check_same.append((1, i,j))
    # 두 과정에서 겹치는 인덱스들은 중복제거
    check_same = list(set(check_same))
    # 인접한게 있다면 , False로 없애준다
    if check_same :
        for check in check_same:
            type, i, j = check
            if type ==0:
                circles[i][j] = False
                circles[i][j-1] = False
            elif type == 1:
                circles[i][j] = False
                circles[i +1][j] = False
    # 인접한게 없다면 평균을 구하고 평균보다 큰 수에서 1 빼고 작은수에 1 더한다
    else:
        cnt = 0
        total =0
        for i in range (n):
            for letter in circles[i]:
                if letter != False:
                    cnt += 1
                    total += letter
        # 나눌 때는 zero divisin error를 항상 생각하자
        if cnt !=0:
            mean_value = total/cnt
            for i in range (n):
                for j in range (m):
                    if circles[i][j] != False:
                        if circles[i][j] > mean_value:
                            circles[i][j] -= 1
                        elif circles[i][j] <mean_value:
                            circles[i][j] += 1

for dt in range (1, t +1):
    x, d, k = map(int, input().split())
    rotate(x, d, k)

# circles는 False 아니면 숫자들로 이루어져있을 것이다
ans = 0
for i in range (n):
    for j in range (m):
        if circles[i][j] != False:
            ans += circles[i][j]
print(ans)