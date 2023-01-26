N=int(input())
x=list(map(int,input().split()))
print(len(x)-len(set(x)))