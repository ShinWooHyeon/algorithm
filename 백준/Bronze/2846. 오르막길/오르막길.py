N=int(input())
road=list(map(int,input().split()))
upper_max=0
on_off=0
for i in range(N-1):
    if on_off:
        if road[i]>=road[i+1]:
            on_off=0
            length=road[i]-road[start]
            if length>upper_max:
                upper_max=length
        else:
            if i==N-2:
                length=road[i+1]-road[start]
                if length>upper_max:
                    upper_max=length
    else:
        if road[i]<road[i+1]:
            on_off=1
            start=i
print(upper_max)