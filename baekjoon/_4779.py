def rec(ep):
    if ep == 1:
        return '-'

    left = rec(ep//3)
    center = ' ' * (ep//3)
    return left+center+left



while True:
    try:
        n = int(input())
        s = ['-' for _ in range(3**n)]

        print(rec(len(s)))
    except:
        break
