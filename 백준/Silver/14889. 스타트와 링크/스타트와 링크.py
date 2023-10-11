# dfs를 통해서 시뮬레이션을 한다 => 이거 연습하기 좋을듯
# 이 문제는 조합으로 푸는게 훨씬 쉬울 거 같지만 일단 시뮬레이션으로 해본다 
n = int(input())
graph = []
total_stat = 0
for i in range (n):
    line = list(map(int, input().split()))
    graph.append(line)
    total_stat += sum(line)

cands = [i for i in range (n)]
m = int(n/2)
min_value = 1e9
members=[]
def dfs(members, cands):
    global n ,m, min_value,total_stat
    if len(members) == m:
        result = 0
        stat_cands = total_stat 
        for i in range (n):
            for member in members:
                stat_cands -= graph[member][i]
                stat_cands -= graph[i][member]
        for i in range (m-1 ):
            for j in range (i+1, m):
                result += graph[members[i]][members[j]] +graph[members[j]][members[i]]
        stat_cands += result
        '''
        print(f'이때 전체 능력치의 합은 {total_stat}')
        print(f'members의 능력치 합은 {result}')
        print(f'cands의 능력치 합은 {stat_cands}')'''     
        min_value = min(min_value, abs(stat_cands - result))
        '''
        print(f'이때 최솟값은 {min_value}')
        print('----------------------------')'''
    else:
        for i in range (len(cands)):
            members.append(cands[i])
            dfs(members, cands[i + 1 :])
            members.pop()

dfs(members, cands)
print(min_value)