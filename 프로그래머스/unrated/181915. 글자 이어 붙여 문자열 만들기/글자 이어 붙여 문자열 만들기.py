def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        print(my_string[i])
        answer += my_string[i]
    return answer