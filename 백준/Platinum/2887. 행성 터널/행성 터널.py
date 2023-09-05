# 행성 터널
#  N개면 계산 횟수 N제곱정도  근데 N제곱 계산하면 메모리 초과함 
# 크루스칼 알고리즘을 사용하는데 x, y, z의 입장에서 따로 따로 고려해야한다
import sys
input = sys.stdin.readline
def find_parent(parent, x):
    if parent[x] != x:
        parent[x]= find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# 노드의 개수 
n= int(input())
parent= [0] * (n + 1)

# 간선 담을 노드
edges= []
result=0

# 부모테이블 상에서 부모를 자기자신으로 초기화 한다
for i in range (n + 1):
    parent[i] = i

# 각 축에 좌표값을 입력받기 위해 나눠서 정리한다
x = []
y = []
z = []
# 연결하기 위해서는 몇번 행성인지를 알아야함 
for i in range (1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))
# 각 축 좌표는 좌표크기, 몇번행성 으로 표시 되어있다 
# 즉 행성이 전부 다르지만 길이가 짧은 순서대로 연결하는 크루스칼알고리즘
x.sort()
y.sort()
z.sort()
# 1번-2번/ 2번-3번/ 3번-4번  
# i번과 i+1을 연결했을때
for i in range (n-1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i+1][1]))

# edge 정렬 필요한데 안했음
edges.sort()

for edge in edges:
    dist, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += dist

print(result)