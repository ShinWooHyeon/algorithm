n= int(input())
# n= 1000이하
cnt =0
if n < 100:
    print(n)
else:
    for i in range(100, n+1):
        if i ==1000:
            continue
        a = i // 100
        b=  (i % 100)//10
        c=  i % 10
        if a-b == b-c :
            cnt +=1
    print(99 + cnt)

