N = int(input())

ans = 0
l = set()
for _ in range(N):
    s = input()
    if s == "ENTER":
        ans += len(l)
        l.clear()
        continue
    l.add(s)

print(ans+len(l))