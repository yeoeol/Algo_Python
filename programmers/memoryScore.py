def solution(name, yearning, photos):
    d = dict(zip(name, yearning))
    answer = []

    for photo in photos:
        summ = 0
        for n in photo:
            if n in d:
                summ += d[n]
        answer.append(summ)

    return answer

print(solution(["may", "kein", "kain", "radi"],
               [5, 10, 1, 3],
               [["may", "kein", "kain", "radi"],
                ["may", "kein", "brin", "deny"],
                ["kon", "kain", "may", "coni"]]))