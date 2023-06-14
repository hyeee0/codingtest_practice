def solution(num_list):
    answer = []
    a = num_list[-1]
    b = num_list[-2]
    if a > b:
        num_list += [a - b]
        print(num_list)
    else:
        num_list += [a*2]
    return num_list