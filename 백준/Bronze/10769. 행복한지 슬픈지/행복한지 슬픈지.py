import sys
input=sys.stdin.readline
sentence=input().strip()
h=sentence.count(':-)')
s=sentence.count(':-(')
if h==s:
    if h==0:
        print('none')
    else:
        print('unsure')
else:
    if h>s:
        print('happy')
    else:
        print('sad')
        