# 수 묶기
# 양수는 큰거 끼리
# 음수는 작은거 끼리
N = int(input())
plus_num = []
minus_num = []
for i in range (N):
    num = int(input())
    if num >0:
        plus_num.append(num)
    else:
        minus_num.append(num)
plus_num.sort(reverse=True)
minus_num.sort()
result = 0
for i in range(len(plus_num)//2):
    if plus_num[2*i] != 1 and plus_num[2*i + 1] !=1 :
        result += plus_num[2*i] * plus_num[2*i + 1]
    else:
        result += plus_num[2*i] + plus_num[2*i + 1]
if len(plus_num)%2 !=0:
    result += plus_num[-1]
for i in range(len(minus_num)//2):
    result += minus_num[2*i] * minus_num[2*i+1]
if len(minus_num)%2 !=0:
    result += minus_num[-1]

print(result)
