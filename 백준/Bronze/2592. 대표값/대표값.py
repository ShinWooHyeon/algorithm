import sys
from collections import Counter
input=sys.stdin.readline
x=[int(input())for _ in range(10)]
print(int(sum(x)/len(x)))
print(Counter.most_common(Counter(x),1)[0][0])