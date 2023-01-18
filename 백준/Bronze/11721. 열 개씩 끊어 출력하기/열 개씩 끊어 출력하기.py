word=input()
n=0
while True:
    n+=10
    print(word[n-10:n])
    if (n-10 <len(word))and (len(word)<=n):
        break