import sys
face='(^0^)'
x=sys.stdin.readline().split(face)
print(x[0].count('@'),end=' ')
print(x[1].count('@'))