def solution(wallpaper):
    minx = 1e9
    miny = 1e9
    maxx = -1e9
    maxy = -1e9
    h = len(wallpaper)
    w = len(wallpaper[0])
    for i in range (h):
        for j in range (w):
            if wallpaper[i][j] == '#':
                minx = min(i, minx)
                miny = min(j, miny)
                maxx = max(i, maxx)
                maxy = max(j, maxy)
    answer = [minx, miny, maxx+1, maxy+1]
    return answer