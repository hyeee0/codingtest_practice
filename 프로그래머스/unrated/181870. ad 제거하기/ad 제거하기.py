def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if not 'ad' in strArr[i]:
            answer.append(strArr[i])
    return answer