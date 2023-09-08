# 크기가 N * N 인 배열 
N, K = int(input()), int(input())
start, end = 1, K
# K번째 수는 K 보다 무조건 같거나 작을 수 밖에 없다. 이해 잘 안가서 제곱수 기준으로 대충 받아들이자 


while start <= end:
    mid = (start + end) // 2
    
    temp = 0 # mid보다 작거나 같은 수
    # 행 기준으로 계산한다
    for i in range(1, N+1):
        temp += min(mid // i, N)

    # mid 보다 작은 숫자를 계산했는데 그게 k보다 크거나 같으면 
    # 위 while문이 종료할때 answer에 있는 mid가 답이기 때문    
    if temp >= K:
        answer= mid
        end = mid -1
    else:
        start =mid + 1
print(answer)