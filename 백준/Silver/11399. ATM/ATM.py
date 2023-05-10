n = int(input())  
ps = list(map(int, input().split()))  
ps.sort()  
ans = 0  

for x in range(1, n+1):
    ans += sum(ps[0:x]) 
print(ans)  