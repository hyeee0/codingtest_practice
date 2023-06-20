def solution(my_string):
    answer = []
    a = ['']
    b = my_string.split(' ')
    answer = [i for i in b if i not in a]
    return answer