def solution(x):
    answer = True
    num = 0
    x1 = str(x)
    for i in x1:
        num += int(i)
    if x % num == 0:
        answer = answer
    else:
        answer = False
    return answer