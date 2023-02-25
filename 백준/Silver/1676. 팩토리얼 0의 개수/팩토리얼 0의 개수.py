import sys
input=sys.stdin.readline
N=int(input())
n_f=1
for i in range(1,N+1):
    n_f*=i
str_n_f=str(n_f)
cnt=0
for j in range(1,len(str_n_f)+1):
    if str_n_f[-1*j]=='0':
        cnt+=1
    else:
        print(cnt)
        break