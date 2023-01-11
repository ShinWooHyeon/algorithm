a=int(input())
b=input()
s=0
for k in range(a):
    s+=(ord(b[k])-96)*(31**k)
print(s)    