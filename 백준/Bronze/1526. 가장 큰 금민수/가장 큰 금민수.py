import sys
input=sys.stdin.readline
N=int(input())
num=4
ans=0
while num<= N:
    if str(num).replace('7','').replace('4','')=='':
        ans=str(num)
    num+=1
print(ans)