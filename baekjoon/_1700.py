n, k = map(int, input().split())
elec = list(map(int, input().split(' ')))

concent = []
ans = 0

for i in range(k):
    if elec[i] in concent:
        continue
    if len(concent) < n:
        concent.append(elec[i])
        continue

    prior = []
    for c in concent:
        if c in elec[i:]:
            prior.append(elec[i:].index(c))
        else:
            prior.append(101)
    target = prior.index(max(prior))
    concent.remove(concent[target])
    concent.append(elec[i])
    ans += 1
print(ans)
