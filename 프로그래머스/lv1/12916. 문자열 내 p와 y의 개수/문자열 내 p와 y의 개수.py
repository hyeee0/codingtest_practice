def solution(s):
    s = s.lower()
    if s.count('p') != s.count('y'):
        answer = False
    else:
        answer = True
    return answer