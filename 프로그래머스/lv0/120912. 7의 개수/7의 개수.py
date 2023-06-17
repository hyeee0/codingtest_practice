def solution(array):
    answer = 0
    for i in range(len(array)):
        s = str(7)
        num = str(array[i])
        if s in num:
            answer += num.count(s)
    return answer
