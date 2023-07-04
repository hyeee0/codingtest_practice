def solution(my_string):
    answer = ''
    temp = list(my_string)
    temp = list(reversed(temp))
    answer = (''.join(temp))
    return answer