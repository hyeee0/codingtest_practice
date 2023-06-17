def solution(my_string):
    answer = ''
    a = list(dict.fromkeys(my_string))
    answer = ''.join(a)
    return answer