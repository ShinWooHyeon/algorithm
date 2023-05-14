import sys
input = sys.stdin.readline
dp_list = [0] * 11
dp_list[1] = 1
dp_list[2] = 2
dp_list[3] = 4
for i in range(4, 11):
    dp_list[i] = sum(dp_list[i-3:i])

T = int(input())
for _ in range(T):
    print(dp_list[int(input())])