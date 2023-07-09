import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start):
    heap = []
    heappush(heap, [0, start])
    dp = [inf] * (n + 1)
    dp[start] = 0
    while heap:
        w, now = heappop(heap)
        for n_n, wei in graph[now]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
    return dp

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])

    x = []
    for _ in range(t):
        x.append(int(input()))

    s_ = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)
    ans = []

    for i in x:
        if s_[g] + g_[h] + h_[i] == s_[i] or s_[h] + h_[g] + g_[i] == s_[i]:
            ans.append(i)
    
    ans.sort()
    print(*ans)