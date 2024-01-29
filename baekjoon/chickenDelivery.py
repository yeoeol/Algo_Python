import sys
from sys import stdin
from itertools import combinations

"""
1. 집 좌표 저장하기(1의 위치)
2. 집 하나 당 모든 치킨 집 까지의 거리 저장하기(2의 위치) -> 가장 작은 거리 저장
3. 치킨거리의 합 계산
4. 치킨 집을 한 곳 폐업시키고 다시 2부터 반복
5. 최솟값 계산 
"""


def solution():
    answer = sys.maxsize

    n, m = map(int, stdin.readline().split())
    l = []
    house = []
    chicken = []

    for _ in range(n):
        l.append(list(map(int, stdin.readline().split())))

    for i in range(n):
        for j in range(n):
            if l[i][j] == 1:
                house.append((i, j))
            elif l[i][j] == 2:
                chicken.append((i, j))

    for c in combinations(chicken, m):
        sum = 0
        for i in range(len(house)):
            chicken_len = sys.maxsize
            for j in range(m):
                chicken_len = min(abs(house[i][0] - c[j][0]) + abs(house[i][1] - c[j][1]), chicken_len)
            sum += chicken_len
        answer = min(sum, answer)

    return answer

print(solution())
