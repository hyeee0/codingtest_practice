def solution(numbers):
    answer = -1
    num_add = 0
    for i in numbers:
        num_add += i
    answer = 45 - num_add
    return answer