answer = 0
left = 13
right = 17

for n in range(left, right+1):
    summ = 1
    for i in range(1, n//2+1):
        if n % i == 0:
            summ += 1
    print("n = ", n)
    print("summ = ", summ)

    if summ % 2 == 0:
        answer += n
    else:
        answer -= n

