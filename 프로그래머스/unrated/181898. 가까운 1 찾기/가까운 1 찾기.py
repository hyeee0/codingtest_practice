def solution(arr, idx):
    answer = -1
    for i, j in enumerate(arr):
        if idx <= i and j == 1:
            return i
    return answer