def solution(strArr):
    answer = []
    temp = []
    for i in ((strArr)):
        temp.append(len(i))
    for i in set(temp): # set 중복을 허용 X -> 1,2,3만 리스트에 존재
        answer.append(temp.count(i)) # 1글자 2개, 2글자 2개, 3글자 1개
    return max(answer)