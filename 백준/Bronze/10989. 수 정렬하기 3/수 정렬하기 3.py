import sys
n = int(sys.stdin.readline())
n_list=[0]*10000
for k in range (n):
    x=int(sys.stdin.readline())
    n_list[x-1]+=1
for j in range(10000):
    if n_list[j]!=0:
        for m in range(n_list[j]):
            print(j+1)