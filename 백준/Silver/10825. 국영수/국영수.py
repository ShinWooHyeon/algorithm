# 국영수 
import sys

input = sys.stdin.readline
n = int(input())
student = []

for i in range (n):
    name, k, e, m = input().split()
    student.append([name, int(k), int(e), int(m)])
student.sort(key= lambda x: (-1 * x[1], x[2], -1 * x[3] , x[0]))

for i in range (n):
    print(student[i][0])