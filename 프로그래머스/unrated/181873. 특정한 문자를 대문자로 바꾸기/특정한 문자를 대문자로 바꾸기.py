def solution(my_string, alp):
    answer = ''
    if alp in my_string:
        alp1 = alp.upper()
        answer = my_string.replace(alp, alp1)
    else:
        answer = my_string
    return answer