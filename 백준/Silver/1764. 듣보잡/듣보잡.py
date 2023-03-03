import sys
input=sys.stdin.readline
N,M=map(int,input().split())
dict={}
for i in range (N+M):
    order=input().strip()
    if order in dict:
        dict[order]+=1
    else:
        dict[order]=1
ans=sorted(dict.items(), key=lambda x :(x[1],x[0]))
cnt=0
ans_list=[]
for j in ans:
    if j[1]==2:
        cnt+=1
        ans_list.append(j[0])
print(cnt)
for k in ans_list:
    print(k)    