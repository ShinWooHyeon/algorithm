# 실습 4번
a=['+']*5
a[0]='#'
print(''.join(a))
for i in range(4):
    a[i],a[i+1]=a[i+1],a[i]
    print(''.join(a))