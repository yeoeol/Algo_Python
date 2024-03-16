n, k = map(int, input().split())

if k < 5:
    print(0)
    exit()
if k == 26:
    print(n)
    exit()


ans = 0
words = [set(input()) for _ in range(n)]
learn = [0 for _ in range(26)]
for i in ['a', 'c', 'n', 'i', 't']:
    learn[ord(i)-ord('a')] = 1

for _ in range(n):
    st = input()
    st = st[4:len(st)-4]
    for i in set(st):
        if l[ord(i)-ord('a')] < 1:
            l[ord(i)-ord('a')] += 1
    if sum(l) <= k:
        ans += 1


print(ans)