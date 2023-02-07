import sys
input=sys.stdin.readline
N=int(input())
stick_list=[]
for _ in range (N):
    stick_list.append(int(input()))
front=stick_list.pop()
cnt=1
for i in range (N-1):
    next_stick=stick_list.pop()
    if next_stick>front:
        front=next_stick
        cnt+=1
print(cnt)