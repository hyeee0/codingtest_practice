def solution(num_list):
    answer = []
    odd = 0
    even = 0
    for i in num_list:
        if (i % 2 == 0): # 짝수
            even += 1
        else: # 홀수
            odd += 1
    answer = [even, odd] # 짝수, 홀수
    return answer