# 백준 과제
# 하루에 1과제 해결 가능,
# 과제마감일까지 남은 일수 ,과제의 점수 
# d로 dp 리스트를 만들고 count 한다 ?
# 처리할때마다 시간 기록 
# 정렬하고 
import sys
input = sys.stdin.readline
N = int(input())
work_list = []
period = 0
for i in range (N):
    a, b = map(int, input().rstrip().split())
    work_list.append((a, b))
    if period < a:
        period = a
# 위는 에러 가능성 x

work_list.sort(key = lambda x : (-x[1], x[0]))
work_check= [False] * (period + 1)
point = 0
for work in work_list:
    for i in range(work[0], 0, -1):
        if not work_check[i] :
            work_check[i] = True
            point += work[1]
            break
print(point)
