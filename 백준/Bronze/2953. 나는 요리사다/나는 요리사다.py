import sys
input=sys.stdin.readline
winner=0
winner_point=0
for i in range (1,6):
    point=sum(map(int,input().split()))
    if point>winner_point:
        winner_point=point
        winner=i
print(winner,winner_point)
        