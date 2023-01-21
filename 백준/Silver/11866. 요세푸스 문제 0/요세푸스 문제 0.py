from collections import deque
all_queue = deque()
ans = []

n, k = map(int, input().split())

for i in range(1, n+1):
    all_queue.append(i)

while all_queue:
    for i in range(k-1):
        all_queue.append(all_queue.popleft())
    ans.append(all_queue.popleft())

print("<",end='')
for i in range(len(ans)-1):
    print("%d, "%ans[i], end='')
print(ans[-1], end='')
print(">")