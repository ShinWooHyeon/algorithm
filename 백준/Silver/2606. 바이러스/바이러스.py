import sys
input=sys.stdin.readline
def dfs_cnt(start):
    n=int(input())
    l=int(input())
    graph=[[] for _ in range(n+1)]
    for i in range (l):
        v1,v2=map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    visit_check=[False]*(n+1)
    stack=[start]
    visit_check[start]=True
    while stack:
        visit=stack.pop()
        for next in graph[visit]:
            if not visit_check[next]:
                visit_check[next]=True
                stack.append(next)
    print(visit_check.count(True)-1)
dfs_cnt(1)