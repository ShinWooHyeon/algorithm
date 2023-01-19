import sys
N=int(sys.stdin.readline())
x=[]
for i in range (N):
    a,b=sys.stdin.readline().split()
    x.append([int(a),b])
x.sort(key=lambda x:x[0])
for i in x:
    print(*i)