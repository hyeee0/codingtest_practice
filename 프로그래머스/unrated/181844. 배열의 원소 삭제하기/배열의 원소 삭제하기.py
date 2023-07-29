def solution(arr, delete_list):
    answer = []
    for i in arr:
        answer.append(i)
        if i in delete_list:
            answer.remove(i)
    return answer