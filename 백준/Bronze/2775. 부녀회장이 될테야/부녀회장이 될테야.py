T=int(input())
for i in range(T):
    k=int(input())
    n=int(input())
    x=[list(range(1,n+1))]
    for j in range(1,k+1): #1~2 까지 중에서
        b=[[]]
        for m in range(1,n+1):   #1부터 3호까지 중에서
            b[0].append(sum(x[j-1][:m])) #1층에 먼저
        x.extend(b) 
    print(x[k][n-1])    