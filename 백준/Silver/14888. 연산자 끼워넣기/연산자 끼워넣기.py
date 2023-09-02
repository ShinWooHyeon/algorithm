# 연산자 끼워넣기
# 중복순열? 그냥 순열로 해도 괜찮을거같은데
from itertools import permutations
import sys
input =sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))

cal_4= ['+','-','*','/']
cal_zip=list(map(int,input().split()))
cal_list=[]
for i in range(4):
    for j in range (cal_zip[i]):
        cal_list.append(cal_4[i])
possible_order=list(permutations(cal_list,n-1))
max_result= -int(10e9)
min_result= +int(10e9)

for i in possible_order:
    result = num[0]
    for j in range (1, n):
        if i[j-1]=='+':
            result += num[j]
        elif i[j-1]=='-':
            result -= num[j]
        elif i[j-1]=='*':
            result *= num[j]
        else:
            if result >=0:
                result//= num[j]
            else:
                result = (-1 * result)// num[j]  * (-1)

    if result >max_result:
        max_result = result
    if result < min_result:
        min_result = result

print(max_result)
print(min_result)
