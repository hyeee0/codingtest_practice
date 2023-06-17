def solution(i, j, k):
    answer = 0
    for a in range(i, j+1):
        a = str(a)
        k = str(k)
        if k in a:
            answer += a.count(k)
    return answer