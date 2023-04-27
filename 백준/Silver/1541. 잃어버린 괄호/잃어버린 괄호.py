order = input().split('-')
num = []
for i in order:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
ans = num[0]
for j in range(1, len(num)):
    ans -= num[j]
print(ans)