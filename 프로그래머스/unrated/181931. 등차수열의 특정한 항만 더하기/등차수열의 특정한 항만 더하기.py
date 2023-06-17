def solution(a, d, included):
    answer = 0
    for i in range(1, len(included)+1):
        if included[i-1] == True:
            answer += a + (d*(i-1))
        else:
            answer += 0
    return answer