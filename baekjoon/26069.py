n = int(input())

meet = ["ChongChong"]

for i in range(n):
    a, b = input().split()
    if a in meet:
        meet.append(b)
    elif b in meet:
        meet.append(a)
print(len(set(meet)))