def solution(X, Y):
    answer = ''
    cntX = [0 for _ in range(10)]
    cntY = [0 for _ in range(10)]
    for x in X:
        cntX[int(x)] += 1
    for y in Y:
        cntY[int(y)] += 1

    for i in range(9, -1, -1):
        answer += min(cntX[i], cntY[i])*str(i)
    if answer == '':
        return '-1'
    if answer[0] == '0':
        return '0'
    return answer

x = "100"
y = "203040"
print(solution(x, y))