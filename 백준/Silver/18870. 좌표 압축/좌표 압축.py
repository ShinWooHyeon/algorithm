import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

array_list = sorted(list(set(array)))
dic = {array_list[i] : i for i in range(len(array_list))}
for i in array:
    print(dic[i], end = ' ')