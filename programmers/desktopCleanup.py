def solution(wallpaper):
    a, b = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                a.append(i)
                b.append(j)

    # x좌표 가장 작은거, y좌표 가장 작은거
    # x좌표 가장 큰거+1, y좌표 가장 큰거+1
    return [min(a), min(b), max(a)+1, max(b)+1]

print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))