def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if i % 5 == 0:
            answer.append(i)
            answer = [x for x in answer if set(str(x)) <= set("05")]

    return answer if answer else [-1]