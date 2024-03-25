N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
p = []

def rec(bef, cnt):
    if cnt == M:
        print(' '.join(map(str, p)))
        return
    for i in range(bef, len(arr)):
        p.append(arr[i])
        rec(i, cnt+1)
        p.pop()

rec(0, 0)