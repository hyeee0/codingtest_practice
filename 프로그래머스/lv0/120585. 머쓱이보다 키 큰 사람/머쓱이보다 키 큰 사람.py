def solution(array, height):
    answer = []
    for i in range(len(array)):
        if array[i] > height:
            answer.append(array[i])
        a = len(answer)
    
    return a