def solution(id):
    id = id.lower()

    newid, before = '', ''
    for i in range(len(id)):
        cur = id[i]
        if cur.islower() or cur.isnumeric() or cur in ['-', '_', '.']:
            newid += cur

    while ".." in newid:
        newid = newid.replace('..', '.')

    newid = newid.strip('.')
    if newid.strip() == '':
        newid = 'a'
    if len(newid) >= 16:
        newid = newid[:15]
        newid = newid.rstrip('.')

    while len(newid) <= 2:
        newid += newid[-1]

    return newid

id = "123_.def"

print(solution(id))