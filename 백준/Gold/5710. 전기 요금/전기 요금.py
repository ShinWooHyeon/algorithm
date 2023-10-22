'''
이웃의 사용량과 내사용량을 합쳤을 때 요금
=> 합친 사용량
이웃의 전기요금과의 차이 (절댓값) 겹치는구간이 없어지고 
f(a + b) = x => a +b를 알 수 있다 
f(a) - f(x-a) = y 모르는 문자 a 하나 해결할 수 있을 까 ? 
이진탐색을 생각해보자
0 ~ a +b 까지 중에서  요금이 더 커지려면 a가 더 작아져야 한다, 요금이 더 작아지려면 a가 더 커져야한다

'''
case=[0, 0, 0]
case[0] = 100 * 2
case[1] = case[0] + (10000-100)  * 3
case[2] = case[1] + (1000000- 10000) * 5
def cal_bill(x):
    if x > 1000000:
        bill = case[2] + 7 * (x-1000000)
    elif x >= 10000:
        bill = case[1] + 5 * (x-10000)
    elif x >= 100:
        bill = case[0] + 3 * (x- 100)
    else:
        bill = x * 2         
    return bill
def cal_use(x):
    if x >= case[2]:
        use = 1000000 + int((x -case[2])/7)
    elif x>= case[1]:
        use = 10000 + int((x-case[1])/ 5)
    elif x>= case[0]:
        use = 100 + int((x-case[0]) / 3)
    else:
        use = int(x/ 2)
    return use
def binary_search(total,start, end, target):
    mid = (start + end)//2
    if start > end:
        return None
    # 요금이 더 타겟보다 크다면 mid를 증가시켜야한다, 작다면 mid를 감소시켜야한다
    if cal_bill(total-mid) -cal_bill(mid) == target:
        return mid
    elif cal_bill(total-mid) -cal_bill(mid)> target:
        return binary_search(total, mid +1, end, target)
    else:
        return binary_search(total, start, mid-1, target )

while True:
    a, b = map(int, input().split())
    if a== 0 and b== 0:
        break
    use_2 = cal_use(a)
    answer = binary_search(use_2, 0, use_2, b)
    print(cal_bill(answer))
