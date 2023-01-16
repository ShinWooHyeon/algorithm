import sys
n = int(sys.stdin.readline())
x=[None]*n
for i in range (n):
    a=sys.stdin.readline().strip('\n')
    x[i]=a
k=list(set(x))
k.sort()
k.sort(key=len)
for i in k:
    print(i)
                        