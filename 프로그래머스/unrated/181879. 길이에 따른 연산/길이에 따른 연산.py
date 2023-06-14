def solution(num_list):
    answer = 0
    a = 1
    for i in num_list:
        print(i)
        if (len(num_list)) <= 10:
            a *= i
            answer = a
            print(a)
            
        else:
            answer += i
    return answer