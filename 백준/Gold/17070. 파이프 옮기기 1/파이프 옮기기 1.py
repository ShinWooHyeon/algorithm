import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

HO = 0 #가로
VIR = 1 #세로
DIAG = 2 #대각
cnt = 0

def dfs(nowy, nowx, type):
    global cnt
    if (nowy, nowx) == (n-1, n-1):
        cnt += 1
        return

    if type == HO or type == DIAG:
        if nowx+1 < n and board[nowy][nowx+1] == 0:
            dfs(nowy, nowx+1, HO)
    if type == VIR or type == DIAG:
        if nowy + 1 < n and board[nowy+1][nowx] == 0:
            dfs(nowy+1, nowx, VIR)

    if nowx+1<n and nowy+1<n:
        if board[nowy+1][nowx] == 0 and board[nowy][nowx+1] == 0 and board[nowy+1][nowx+1] == 0:
            dfs(nowy+1, nowx+1, DIAG)


dfs(0, 1, HO)
print(cnt)