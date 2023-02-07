import sys
input=sys.stdin.readline
move={'R':(0,1),'L':(0,-1),'B':(1,0),'T':(-1,0),'RT':(-1,1),'LT':(-1,-1),'RB':(1,1),'LB':(1,-1)}
width='ABCDEFGH'
k,s,N=input().strip().split()
k_place=(8-int(k[1]),width.index(k[0]))
s_place=(8-int(s[1]),width.index(s[0]))
for i in range (int(N)):
    order=move[input().strip()]
    if ((k_place[0]+order[0]) in range(8)) and((k_place[1]+order[1]) in range(8)) :
        if (k_place[0]+order[0],k_place[1]+order[1])==s_place:
            if ((s_place[0]+order[0]) in range(8)) and((s_place[1]+order[1]) in range(8)) :
                k_place=(k_place[0]+order[0],k_place[1]+order[1])
                s_place=(s_place[0]+order[0],s_place[1]+order[1])
        else:
            k_place=(k_place[0]+order[0],k_place[1]+order[1])
print(str(width[k_place[1]])+str(8-k_place[0]))
print(str(width[s_place[1]])+str(8-s_place[0]))