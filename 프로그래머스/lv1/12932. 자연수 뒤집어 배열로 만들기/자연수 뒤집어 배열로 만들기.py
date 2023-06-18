def solution(n):
    answer = []
    n = str(n)
    n = list(n)
    n.reverse()
    for i in n:
        a = int(i)
        answer.append(a)
    
    return answer