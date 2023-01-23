import sys
K=int(sys.stdin.readline().strip())
ans=[]
for i in range(K):
    x=int(sys.stdin.readline().strip())
    if x==0:
        ans.pop()
    else:
        ans.append(x)
print(sum(ans))
                
        
        
