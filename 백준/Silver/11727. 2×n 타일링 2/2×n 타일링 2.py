case = [0, 1, 3]
for i in range(3, 1001): #1000 까지이므로 구간은 1000 까지
  case.append((case[i - 2] * 2) + case[i - 1])
n = int(input())
print(case[n] % 10007)