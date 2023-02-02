import sys
from itertools import combinations
input=sys.stdin.readline
word=input().strip()
making_word=[]
possible=list(combinations(range(1,len(word)),2))
for k in possible:
    a,b= k
    x=word[:a]
    y=word[a:b]
    z=word[b:]
    new_word=[x,y,z]
    for m in range(0,3):
        new_word.append(new_word[m][::-1])
    last_word=''
    for j in range(3,6):
        last_word+=new_word[j]
    making_word.append(last_word)
making_word.sort()
print(making_word[0])
