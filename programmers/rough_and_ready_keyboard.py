from collections import defaultdict

def solution(keymap, targets):
    answer = []
    d = defaultdict(int)

    for key in keymap:
        for i, n in enumerate(key):
            d[n] = i+1 if d[n] == 0 else min(d[n], i+1)

    for target in targets:
        summ = 0
        for t in target:
            if d[t] == 0:
                summ = -1
                break
            summ += d[t]
        answer.append(summ)

    return answer

print(solution(["ABC"], ["XA"]))