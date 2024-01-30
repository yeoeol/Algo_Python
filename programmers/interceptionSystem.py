def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    shoot = -1
    for s, e in targets:
        if s >= shoot:
            answer += 1
            shoot = e

    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))