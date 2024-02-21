dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m = map(int, input().split())
r, c, d = map(int, input().split())

mmap = []
for _ in range(n):
    mmap.append(list(map(int, input().split())))

mmap[r][c] = 2
answer = 1
while True:
    space = False
    for i in range(4):
        moveR = r + dir[i][0]
        moveC = c + dir[i][1]
        if 0 <= moveR < n and 0 <= moveC < m:
            if mmap[moveR][moveC] == 0:
                space = True
                break

    if not space:
        mR = r - dir[d][0]
        mC = c - dir[d][1]
        if 0 > mR or mR >= n or 0 > mC or mC >= m or mmap[mR][mC] == 1:
            break
        if mmap[mR][mC] == 0:
            mmap[mR][mC] = 2
            answer += 1
        r, c = mR, mC
    else:
        d = (d-1)%len(dir)
        mR = r + dir[d][0]
        mC = c + dir[d][1]
        if 0 <= mR < n and 0 <= mC < m:
            if mmap[mR][mC] == 0:
                mmap[mR][mC] = 2
                answer += 1
                r, c = mR, mC

print(answer)