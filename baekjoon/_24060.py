N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
def merge(p, q, r):
    global cnt
    i, j = p, q+1
    tmp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    i = p
    for idx in range(len(tmp)):
        cnt += 1
        if cnt == K:
            print(tmp[idx])
            exit()
        A[i] = tmp[idx]
        i += 1

def merge_sort(p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(p, q)
        merge_sort(q+1, r)
        merge(p, q, r)

merge_sort(0, N-1)

print(-1)