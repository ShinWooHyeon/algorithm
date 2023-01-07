x=[]
for i in range(10):
  x.append(int(input()))
y=[]
for i in x:
    y.append(i%42)
print(len(set(y)))