import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pocket = {}

for i in range(1, n + 1):
    a = input().rstrip()
    pocket[i] = a
    pocket[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(pocket[int(quest)])
    else:
        print(pocket[quest])