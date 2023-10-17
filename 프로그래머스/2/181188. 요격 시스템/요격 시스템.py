# 1.각 미사일 별로 리스트를 만들고
# 2. pop해서 그 미사일 없앨 수 있는 모든 애들에 dfs
# 3. pop한 target을 다시 넣어서 같은 과정 돌입
# 4. 만약에 targets의 길이가 0이라면 그때 min_value 갱신
from copy import deepcopy

def solution(targets, result):
    global min_value
    a, b = targets.pop() 
    cands = []
    for i in range (a, b):
        cands.append(i)
    result += 1
    for cand in cands:
        targets_cand = deepcopy(targets)
        for i in len(targets):
            # 쏜 미사일이 범위안에 있다면 target cand에서 지워버린다 
            if targets[i][0] <= cand < targets[i][1] :
                targets_cand.remove(targets[i])
        # 범위안 미사일을 다 지웠다면, 미사일이 있다면 다음 cand에 대해서 진행한다
        if len(targets_cand) == 0:
            min_value = min(result, min_value)
        else:
            solution(targets_cand, result)

print(0)
                