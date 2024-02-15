def solution(a, b, n):
    answer = 0
    while True:
        if n < a:
            break
        cola = n // a * b
        n %= a
        n += cola
        answer += cola
    return answer

print(solution(2, 1, 20))