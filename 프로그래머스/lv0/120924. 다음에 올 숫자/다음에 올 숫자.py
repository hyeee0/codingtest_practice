def solution(common):
    answer = 0
    num = []
    for i in range(len(common)-1):
        num += [common[i+1] - common[i]]
    if num[0] == num[1]:
        answer = common[-1] + num[0]
    else:
        a = num[1] // num[0]
        answer = common[-1] * a
    return answer