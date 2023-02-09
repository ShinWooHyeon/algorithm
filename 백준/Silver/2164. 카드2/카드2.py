import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
card=deque(range(1,N+1))
if N==1:
    print(1)
else:
    while len(card)>=2:
        card.popleft()
        card.append(card.popleft())
    print(card[0])
    