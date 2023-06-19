def solution(num):
    answer = 0
    num_list = []
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        num_list.append(num)
        answer = len(num_list)
    if len(num_list) > 500:
        answer = -1
    return answer