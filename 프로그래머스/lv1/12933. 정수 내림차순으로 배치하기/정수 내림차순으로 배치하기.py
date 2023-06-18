def solution(n):
    answer = ''
    n = list(str(n))
    n.sort(reverse=True)
    answer = int(''.join(n))
    return answer