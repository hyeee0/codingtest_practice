def solution(ineq, eq, n, m):
    answer = 0
    a = ineq + eq
    
    if a == '>=':
        if n >= m:
            answer = 1
    elif a == '<=':
        if n <= m:
            answer = 1
    elif a == '>!':
        if n > m:
            answer = 1
    elif a == '<!':
        if n < m:
            answer = 1
            
    return answer