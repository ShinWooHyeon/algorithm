N,K =map(int,input().split())
x=N-K
a=1
b=1
for i in range(K):
    a*=N
    N-=1
for j in range(K):
    b*=K
    K-=1
print(int(a/b))