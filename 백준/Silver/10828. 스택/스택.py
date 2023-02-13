import sys
input=sys.stdin.readline

def stack_func():
    n=int(input())
    stack=[]
    for i in range (n):
        order=input().strip().split()
        if len(order)==2:
            if order[0]=='push':
                stack.append(int(order[1]))
        else:
            if order[0]=='pop':
                if len(stack)!=0:
                    print(stack.pop())
                else:
                    print(-1)
            elif order[0]=='size':
                print(len(stack)) 
            elif order[0]=='empty':
                if len(stack)==0:
                    print(1)
                else:
                    print(0)
            else:
                if len(stack)!=0:
                    print(stack[-1])
                else:
                    print(-1)
stack_func()