a,b,c,d=map(int,input().split())
print(min(min(b,abs(b-d)),min(a,abs(c-a))))