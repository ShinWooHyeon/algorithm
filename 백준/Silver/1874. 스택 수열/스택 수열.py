import sys
input=sys.stdin.readline
n = int(input())
stack = []
ans = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:      
        stack.append(cur)
        ans.append("+")
        cur += 1
  

    if stack[-1] == num:    
        stack.pop()         
        ans.append("-")
    else:                   
        print("NO")         
        flag = 1            
        break               

if flag == 0:
    for i in ans:
        print(i)