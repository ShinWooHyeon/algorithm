import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    order = sys.stdin.readline().strip().split()
    
    if len(order) == 1:
        if order[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        func, num = order[0], order[1]
        num= int(num)
        if func == "add":
            S.add(num)
        elif func == "remove":
            S.discard(num)
        elif func == "check":
            print(1 if num in S else 0)
        elif func == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)