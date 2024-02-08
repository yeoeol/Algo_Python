def solution(k, score):
    answer = []
    scores = []
    for i in score:
        scores.append(i)
        if len(scores) > k:
            scores.remove(min(scores))
        answer.append(min(scores))
    return answer


print(solution(4, 	[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))