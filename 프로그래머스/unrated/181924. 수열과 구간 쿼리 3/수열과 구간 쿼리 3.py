def solution(arr, queries):
    answer = []
    for i in queries:
        a, b = i[0], i[1]
        arr[a], arr[b] = arr[b], arr[a]

    return arr