def solution(arr):
    answer = []
    num = len(arr)
    for i in range(0, 11):
        a = 2 ** i
        if num == a:
            answer = arr
            break
        elif num < a:
            b = a - len(arr)

            answer = arr+([0]*b)
            break
    return answer