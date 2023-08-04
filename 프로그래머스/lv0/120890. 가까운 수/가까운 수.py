def solution(array, n):
    answer = 0
    num = 100
    array = sorted(array)
    for i in range(len(array)):
        if abs(array[i] - n) < num:
            answer = array[i]
            num = abs(array[i] - n)
    return answer