N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
visited = [False for _ in range(N+1)]
p = []
def rec(cnt):
    if cnt == M:
        print(' '.join(map(str, p)))
        return
    for i in range(N):
        if not visited[arr[i]]:
            visited[arr[i]] = True
            p.append(arr[i])
            rec(cnt+1)
            p.pop()
            visited[arr[i]] = False

rec(0)