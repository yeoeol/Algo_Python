d = {'*':[3, 4, 5, 2, 3, 4, 1, 2, 3, 1],
     '#':[5, 4, 3, 4, 3, 2, 3, 2, 1, 1],
    1:[0, 1, 2, 1, 2, 3, 2, 3, 4, 4],
     2:[1, 0, 1, 2, 1, 2, 3, 2, 3, 3],
     3:[2, 1, 0, 3, 2, 1, 4, 3, 2, 4],
     4:[1, 2, 3, 0, 1, 2, 1, 2, 3, 3],
     5:[2, 1, 2, 1, 0, 1, 2, 1, 2, 2],
     6:[3, 2, 1, 2, 1, 0, 3, 2, 1, 3],
     7:[2, 3, 4, 1, 2, 3, 0, 1, 2, 2],
     8:[3, 2, 3, 2, 1, 2, 1, 0, 1, 1],
     9:[4, 3, 2, 3, 2, 1, 2, 1, 0, 2],
     0:[4, 3, 4, 3, 2, 3, 2, 1, 2, 0]}

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

answer = ''
left = '*'
right = '#'
for n in numbers:
    if n in [1, 4, 7]:
        answer += 'L'
        left = n
    elif n in [3, 6, 9]:
        answer += 'R'
        right = n
    else:
        d1 = d[left][n-1]
        d2 = d[right][n-1]
        if d1 < d2:
            answer += 'L'
            left = n
        elif d1 > d2:
            answer += 'R'
            right = n
        else:
            if hand == "left":
                answer += 'L'
                left = n
            elif hand == "right":
                answer += 'R'
                right = n
print(answer)