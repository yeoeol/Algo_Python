def rec(l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return rec(l+1, r-1)

T = int(input())
for _ in range(T):
    s = input()
    cnt = 0
    print(rec(0, len(s)-1), cnt)


