def DFS(start):
    if len(s) == m:  # 해당 배열의 길이가 m과 동일해지면 프린트 후 리턴
        print(' '.join(map(str, s)))
        return

    # 반복문 반복시
    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            DFS(i+1)
            s.pop()


n, m = map(int, input().split())
s = []
DFS(1)