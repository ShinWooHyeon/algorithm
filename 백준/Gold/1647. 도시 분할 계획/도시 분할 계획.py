import sys
input=sys.stdin.readline
def find_parent(parent, x):
    if parent[x] != x:
        parent[x]= find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a= find_parent(parent, a)
    b= find_parent(parent, b)
    if a < b:
        parent[b]= a
    else:
        parent[a]=b
n , m = map(int,input().split())
parent=[0] * (n+1)

#간선을 받을 리스트와 비용 담을 결과값 생성
nodes = []
result = 0
#자기 노드 자기로
for i in range(1, n+1):
    parent[i]=i

for i in range (m):
    a, b, cost = map(int, input().split())
    nodes.append((cost,a,b))

nodes.sort()
max_cost=0
indegree=[0]*(n+1)
for i in nodes:
    cost,a,b = i
    if find_parent(parent, a) !=find_parent(parent, b):
        union_parent(parent,a,b)
        if cost>max_cost:
            max_cost=cost
        result+=cost


print(result-max_cost)