n, s = map(int, input().split())
seq = list(map(int, input().split()))

left, right = 0, 0
summ = 0
leng = []

while True:
    if summ >= s:
        leng.append(right-left)
        summ -= seq[left]
        left += 1
    elif right == n:
        break
    else:
        summ += seq[right]
        right += 1

if len(leng) == 0:
    print(0)
else:
    print(min(leng))