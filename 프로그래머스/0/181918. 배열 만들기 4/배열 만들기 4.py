def solution(arr):
    stk = []
    i = 0
    while i < len(arr): # i가 arr의 길이보다 작으면 while을 통해 반복
        if not stk: # stk가 비어있는 경우
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]: # stk의 마지막 원소가 arr[i]보다 작은 경우
            stk.append(arr[i])
            i += 1
        else: # stk의 마지막 원소가 arr[i]보다 크거나 같은 경우
            stk.pop() # stk의 마지막 원소를 제거
    return stk