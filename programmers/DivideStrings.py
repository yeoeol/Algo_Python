def solution(s):
    answer = 0

    prev = ""
    n1, n2 = 0, 0
    for i in range(len(s)):
        if prev == "":
            prev = s[i]
            n1 = 1
            continue

        if prev == s[i]:
            n1 += 1
        else:
            n2 += 1
        if n1 == n2:
            answer += 1
            n1, n2 = 0, 0
            prev = ""
    if prev != "":
        answer += 1
    return answer