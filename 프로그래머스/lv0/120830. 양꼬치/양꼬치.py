def solution(n, k):
    answer = 0
    
    z = n // 10
    
    x = n * 12000
    y = (k-z) * 2000
    answer = x + y
    
    return answer