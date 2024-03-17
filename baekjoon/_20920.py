import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
voca_num = {}
for i in range(N):
    s = input().rstrip()
    if len(s) < M:
        continue
    if s in voca_num:
        voca_num[s] += 1
    else:
        voca_num[s] = 1

c = sorted(voca_num.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for a in c:
    print(a[0])
