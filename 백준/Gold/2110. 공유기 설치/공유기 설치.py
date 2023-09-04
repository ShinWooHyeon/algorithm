# 가장 인접한 두 공유기 사이릐 거리를 최댓값으로 탐색해야 한다
# 가장 인접한 공유기 사이의 거리를 조절하며 , C 보다 많은 개수로 공유기 설치할 수 있는지 확인한다
#  떡볶이 떡 만들기와 문제가 유사하다 
import sys
input = sys.stdin.readline
n, c = map(int, input().split())
array = [int(input()) for _ in range (n)]
array.sort() # 이진탐색을 위해서는 정렬이 필요하다

# 공유기 사이의 가능한 거리는 최소 1 (같은 장소는 아니니까) 최대 최댓값- 최솟값 (정렬된 순서에서)
start = 1 # 최솟값
end= array[-1] - array[0]
result  =0

while start <= end:
    mid = (start + end) // 2 
    # 앞에서부터 설치하므로 시작 좌표를 변수에 할당
    value = array[0]
    count = 1 # 공유기의 개수
    # 가능한 최대거리의 중간값을 기준으로 앞에서 공유기를 설치한다
    # 인덱스 기준이 여기서는 아니라는 점을 잘 생각하자
    
    for i in range (1, n):
        if array[i] >= value + mid:
            value = array[i] # 공유기 설치되었으면 설치된 좌표를 value에 할당, 왜냐면 다음 공유기 설치때는 그 value랑 비교해야 되니까
            count += 1
    if count >= c : # C개 이상의 공유기 왜 등호가 아니라 부등호도 들어가냐면 추가로 설치한 경우와 설치 안한경우 모두 MID를 만족할 수 있기 때문
        # 이부분의 식은 가능한 경우를 저장하고 거리의 최댓값 확인을 위해 start를 증가시켜 거리를 증가시키는 과정이다
        start = mid +1 
        result = mid # 결과값은 일단 저장
    else: # 공유기 설치가 불가하면 오히려 거리를 줄여야한다 즉 확인해볼 수 있는 거리의 최댓값을 미드보다 1감 소시킨다  
        end = mid -1 # 거
print(result)