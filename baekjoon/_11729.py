N = int(input())
k = 0

#참고 자료
#https://kbwplace.tistory.com/115
#https://study-all-night.tistory.com/6
def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, start, 6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)

#최소한의 이동 값은 n = 1일 때 1, n = 2일 때 3, n = 3일 때 7, n=4일 때 15 이므로 (2^n - 1)의 식이 완성됨
print(2**N-1)
hanoi(N, 1, 3)
