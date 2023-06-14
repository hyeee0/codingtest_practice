def solution(num_list, n):
    answer = 0
    for i in num_list:
        print(i)
        if i == n:
            answer = 1
    return answer