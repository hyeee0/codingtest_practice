def solution(n):
    answer = []
    while n != 1:
        if n % 2 == 0:
            answer += [n]
            n = n // 2
        elif n % 2 == 1:
            answer += [n]
            n = 3 * n + 1
    answer += [1]       
    return answer