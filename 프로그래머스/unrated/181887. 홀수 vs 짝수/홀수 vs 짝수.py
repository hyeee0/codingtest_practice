def solution(num_list):
    answer = 0
    a = sum(num_list[::2]) #짝수
    b = sum(num_list[1::2]) #홀수
    if a > b:
        answer = a
    else:
        answer = b
    return answer