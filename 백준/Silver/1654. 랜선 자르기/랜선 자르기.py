import sys
input=sys.stdin.readline
K,N=map(int,input().split())
line=[int(input() )for _ in range(K)]
start=1
end=max(line)
while start<=end:
    mid=(start+end)//2
    line_num=0
    for i in line:
        line_num+=i//mid
    if line_num>=N:
        start=mid+1
    else:
        end=mid-1
print(end)