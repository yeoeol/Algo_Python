def solution(cards1, cards2, goal):
    answer = 'Yes'

    for g in goal:
        if len(cards1) != 0 and cards1[0] == g:
            cards1.pop(0)
        elif len(cards2) != 0 and cards2[0] == g:
            cards2.pop(0)
        else:
            answer = "No"
            break

    return answer