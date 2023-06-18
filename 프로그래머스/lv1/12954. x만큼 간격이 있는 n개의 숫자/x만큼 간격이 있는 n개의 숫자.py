def solution(x, n):
    answer = []
    a = 1
    num_start = a * x

    for i in range(1, n+1):
        x = num_start * i
        answer.append(x)
    return answer