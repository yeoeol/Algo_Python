N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
p = []
def rec(start, cnt):
    if cnt == M:
        print(' '.join(map(str, p)))
        return
    for i in range(start, N+1):
        p.append(arr[i-1])
        rec(i+1, cnt+1)
        p.pop()

rec(1, 0)