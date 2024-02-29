def solution(lottos, win_nums):
    answer = []

    a = 7
    for i in win_nums:
        if i in lottos:
            a -= 1

    c = lottos.count(0)
    if c == 6:
        return [1, 6]
    if a == 7:
        return [6, 6]
    else:
        answer.append(a-c)
        answer.append(a)

    return answer

lotto = [1, 2, 3, 4, 5, 6]
win = [7, 8, 9, 10, 11, 12]

print(solution(lotto, win))