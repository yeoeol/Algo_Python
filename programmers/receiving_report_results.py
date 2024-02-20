def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    r = {x : 0 for x in id_list}

    for item in set(report):
        s = item.split(' ')
        r[s[1]] += 1

    for i in set(report):
        s = i.split()
        if r[s[1]] >= k:
            answer[id_list.index(s[0])] += 1

    return answer

id = ["muzi", "frodo", "apeach", "neo"]
re = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
print(set(re))
k = 2
print(solution(id, re, k))