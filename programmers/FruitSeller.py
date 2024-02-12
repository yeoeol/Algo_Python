def solution(k, m, score):
    score.sort(reverse=True)
    summ = 0

    for i in range(0, len(score), m):
        s = score[i:i+m]
        if len(s) != m:
            break
        summ += s[-1] * m
    return summ

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))
