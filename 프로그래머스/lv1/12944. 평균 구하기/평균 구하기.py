def solution(arr):
    answer = 0
    a = 0
    for i in arr:
        a += i
        print(answer)
        answer = a/(len(arr))
    return answer