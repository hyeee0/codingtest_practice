def solution(quiz):
    
    result = []

    for i in quiz:
        a, b = i.split("=") 
        # = 기준으로 나눠준다. a는 X [연산자] Y, b는 Z -> 이거 찾아봄 separator 기준으로 나누는 법
        
        a = a.split() # 'X, [연산자], Y'가 각각 다 나눠짐


        if a[1] == "+": # a[1]=연산자 이니깐 + 일때
            Z = int(a[0]) + int(a[2])

        elif a[1] == "-": # a[1]=연산자 이니깐 - 일때
            Z = int(a[0]) - int(a[2])

        if Z == int(b):
            result.append("O")
        else:
            result.append("X")
    
    return result