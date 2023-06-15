def solution(a, b):
    answer = 0
    a = str(a)
    b = str(b)
    if a + b > b + a:
        c = a + b
        answer = int(c)
    else:
        c = b + a
        answer = int(c)
    return answer