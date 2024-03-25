N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
p = []

def rec(cnt):
    if cnt == M:
        print(' '.join(map(str, p)))
        return
    for i in arr:
        p.append(i)
        rec(cnt+1)
        p.pop()

rec(0)