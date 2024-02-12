def solution(number, limit, power):
    l = [1]
    for i in range(2, number+1):
        n = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                n += 2
                if j**2 == i:
                    n -= 1
        if n > limit:
            n = power
        l.append(n)
    print(l)
    return sum(l)

print(solution(10, 3, 2))