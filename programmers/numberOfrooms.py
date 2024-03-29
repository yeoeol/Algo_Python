from collections import defaultdict

def solution(arrows):
    answer = 0
    visited = defaultdict(list)
    x, y = 0, 0
    dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

    for arrow in arrows:
        for _ in range(2):
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            if (nx, ny) in visited and (x, y) not in visited[(nx, ny)]:
                answer += 1
            visited[(nx, ny)].append((x, y))
            visited[(x, y)].append((nx, ny))
            x, y = nx, ny

    return answer

