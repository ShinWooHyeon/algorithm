import sys
from collections import deque
input=sys.stdin.readline

def deque_func():
    n=int(input())
    deque_list=deque([])
    for i in range (n):
        order=input().strip().split()
        if len(order)==2:
            if order[0]=='push':
                deque_list.append(int(order[1]))
        else:
            if order[0]=='pop':
                if len(deque_list)!=0:
                    print(deque.popleft(deque_list))
                else:
                    print(-1)
            elif order[0]=='size':
                print(len(deque_list)) 
            elif order[0]=='empty':
                if len(deque_list)==0:
                    print(1)
                else:
                    print(0)
            elif order[0]=='front':
                if len(deque_list)!=0:
                    print(deque_list[0])
                else:
                    print(-1)
            else:
                if len(deque_list)!=0:
                    print(deque_list[-1])
                else:
                    print(-1)
deque_func()