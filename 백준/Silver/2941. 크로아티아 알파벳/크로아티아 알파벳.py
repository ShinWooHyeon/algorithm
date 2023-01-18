import sys
x=['c=','c-','dz=','d-','lj','nj','s=','z=']
crs=sys.stdin.readline().strip('\n')
s=0
for i in x:
    s+=crs.count(i)
ans=len(crs)-s
print(ans)