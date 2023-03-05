import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic = {}
for _ in range(N):
    site, ps = input().split()
    dic[site] = ps

for _ in range(M):
    print(dic[input().rstrip()])