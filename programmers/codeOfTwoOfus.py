def solution(string, skip, index):
    answer = ''

    alpha = set(chr(i) for i in range(97, 123))
    alpha = sorted(alpha-set(skip))
    for s in string:
        idx = alpha.index(s)+index
        if idx >= len(alpha):
            idx %= len(alpha)
        answer += alpha[idx]

    return answer

print(solution("aukks", "wbqd", 5))
print(solution("y", "baz", 1))
