dirr = {'E':(0, 1), 'W':(0, -1), 'S':(1, 0), 'N':(-1, 0)}

def solution(park, routes):
    x = len(park)
    y = len(park[0])

    for i, p in enumerate(park):
        if "S" in p:
            curX, curY = (i, p.index("S"))

    for route in routes:
        d, n = route.split()
        n = int(n)
        flag = True
        for i in range(1, n+1):
            nx, ny = curX+dirr[d][0]*i, curY+dirr[d][1]*i
            if nx < 0 or nx >= x or ny < 0 or ny >= y:
                flag = False
                break
            if park[nx][ny] == 'X':
                flag = False
                break
        if flag:
            curX += dirr[d][0]*n
            curY += dirr[d][1]*n

    return [curX, curY]

park = ["SOO","OXX","OOO"]
routes = ["E 2","S 2","W 1"]
print(solution(park, routes))
