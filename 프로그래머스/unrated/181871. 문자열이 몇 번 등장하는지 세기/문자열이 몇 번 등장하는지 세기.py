def solution(myString, pat):
    answer = 0
    for i, j in enumerate(myString):
        if (myString[i:].startswith(pat)) == True:
            answer += 1
    return answer