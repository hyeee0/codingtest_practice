def solution(arr, queries):
    answer = arr[:] # 원본 배열 복사
    
    for query in queries:
        s, e, k = query
        for i in range(s, e + 1): # s ≤ i ≤ e 조건
            if i % k == 0: # i가 k의 배수 조건
                answer[i] += 1
    return answer