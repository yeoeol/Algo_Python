def solution(seq, k):
    answer = []

    length = len(seq)
    maxx, end = 0, 0

    for i in range(length):
        while maxx < k and end < length:
            maxx += seq[end]
            end += 1

        if maxx == k:
            answer.append([i, end-1, end-1-i]) #시작점, 끝점, 길이

        maxx -= seq[i]

    answer.sort(key=lambda x : x[2])
    print(answer)
    return answer[0][:2]
    return answer



print(solution([1,2,3,4,5], 7))