import sys
input=sys.stdin.readline
passenger_num=0
max_passenger=0
for i in range(4):
    g,r=map(int,input().split())
    passenger_num+=r-g
    if passenger_num>max_passenger:
        max_passenger=passenger_num
print(max_passenger)