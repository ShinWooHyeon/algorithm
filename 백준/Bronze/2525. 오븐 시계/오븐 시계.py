import sys
input=sys.stdin.readline
A,B=map(int,input().split())
C=int(input())
time_hour=C//60
time_minute=C%60
if B+time_minute >=60:
    total_minute=(B+time_minute)%60
    time_hour+=1
else:
    total_minute=B+time_minute
total_hour= (A+time_hour)%24
print(total_hour,total_minute)