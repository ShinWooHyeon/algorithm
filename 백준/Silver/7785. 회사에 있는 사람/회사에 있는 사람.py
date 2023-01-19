import sys
from collections import Counter
T=int(sys.stdin.readline().strip())
g_log={}
for i in range (T):
    a,b=sys.stdin.readline().strip().split()
    if a not in g_log.keys():
        g_log[a]=b
    else:
        del g_log[a]
work_list=sorted(list(g_log.keys()),reverse=True)
for i in work_list:
    print(i)