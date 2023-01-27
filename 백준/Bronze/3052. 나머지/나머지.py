import sys
x=[]
for i in range(10):
  x.append(int(sys.stdin.readline())%42)
print(len(set(x)))