def solution(s):
    answer = []
    dic = dict()

    for idx, item in enumerate(s):
        if item not in dic:
            answer.append(-1)
        else:
            answer.append(idx-dic[item])
        dic[item] = idx


    return answer