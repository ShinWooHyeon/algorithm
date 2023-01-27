import sys
n = int(sys.stdin.readline())
x=[None]*n
for i in range (n):
    x[i]=sys.stdin.readline().strip('\n')
k=list(set(x)) 
k.sort()         
k.sort(key=len)  
for i in k:
    print(i)
