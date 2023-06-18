def solution(n):
    answer = -1
    a = n ** (1/2)
    num = int(a)
    if a == num:
        answer = (num+1)**2
    return answer