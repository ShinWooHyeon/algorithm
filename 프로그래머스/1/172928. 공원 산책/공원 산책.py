def solution(park, routes):
    h = len(park)
    w = len(park[0])
    check = False
    answer= []
    for i in range (h):
        for j in range (w):
            if park[i][j] == 'S':
                sx, sy = i, j
                check =True
                break
        if check:
            break
    for i in range (len(routes)):
        a, b = routes[i].split()
        if a =='E':
            dx, dy = 0, 1
        elif a == 'W':
            dx, dy= 0, -1
        elif a == 'N':
            dx, dy = -1, 0
        elif a == 'S':
            dx, dy = 1, 0
        for j in range (1,int(b) +1):
            nx = sx + j * dx
            ny = sy + j * dy
            if 0<= nx < h and 0 <= ny < w and park[nx][ny] != 'X':
                continue
            else:
                break
        else:
            sx = sx + int(b) * dx
            sy = sy + int(b) * dy
    answer.append(sx)
    answer.append(sy)
    return answer