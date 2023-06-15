def solution(a, b):
    answer = 0
    a1 = str(a)
    b1 = str(b)
    c = int(a1+b1)
    d = 2*a*b
    if c > d:
        answer = c
    else:
        answer = d
    return answer