import heapq
import math
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = math.inf

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

dist = [INF for _ in range(n + 1)]
def dijkstra(s):
    dist[s] = 0
    queue = [(0, start)]
    while queue:
        w, cur = heapq.heappop(queue)
        if dist[cur] < w:
            continue
        for dest, wei in graph[cur]:
            cost = dist[cur] + wei
            if dist[dest] > cost:
                dist[dest] = cost
                heapq.heappush(queue, (cost, dest))

dijkstra(start)
print(dist[end])


