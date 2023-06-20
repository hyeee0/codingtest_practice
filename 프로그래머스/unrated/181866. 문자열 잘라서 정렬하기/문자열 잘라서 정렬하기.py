def solution(myString):
    answer = []
    a = ['']
    answer = (myString.split('x'))
    answer.sort()
    answer = [i for i in answer if i not in a] 
    return answer