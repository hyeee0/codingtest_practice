def solution(n):
    answer = 0
    slice = 6
    
    for i in range(max(n, slice), (n*slice)+1): # 최소공배수를 구해보자!
        if (i % slice == 0) and (i % n == 0):
            print(i)
            answer = i / 6
            break
        
    
    return answer