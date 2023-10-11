# 저번에도 시간초과로 포기했는데 dfs를 시뮬레이션에 적극 활용할 수 있다
n = int(input())
num_list = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
min_value = 1e9
max_value = -1e9


def dfs (i, now):
    global plus, minus, mul, div, min_value, max_value
    if i == n :
        min_value = min(now, min_value)
        max_value = max(now, max_value)
    # 남아 있는 기호만큼 쓴다 기호가 없다면 dfs로 확장될 수 없다 
    else:
        if plus > 0:
            # 사용가호 개수 1개 더해주고 거기서 dfs
            plus -= 1
            dfs(i + 1, now +num_list[i])
            # 모든 경우를 다 해보려면 plus를 사용하지 않고 나머지를 사용했을 때도 해봐야 하므로 다시 초기화 시켜야 한다 
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i + 1, now - num_list[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * num_list[i])
            mul += 1
        if div >0:
            div -=1
            dfs(i + 1, int(now / num_list[i]))
            div += 1

dfs(1, num_list[0])
print(max_value)
print(min_value)