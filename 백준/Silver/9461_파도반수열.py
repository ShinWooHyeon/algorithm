T = int(input())
pd = [0 for i in range(101)]
pd[1] = 1
pd[2] = 1
pd[3] = 1
for i in range(0, 98):
    pd[i + 3] = pd[i] + pd[i + 1]
for i in range(T):
    n = int(input())
    print(pd[n])