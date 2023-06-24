def solution(code):
    answer = ''
    mode = 0
    
    for i in range(len(code)):
        if mode == 0: # mode가 0인 경우 짝수 인덱스를 추가
            if code[i] != '1' and i % 2 == 0:
                answer += code[i]
            elif code[i] == '1':
                mode = 1
        else:
            if code[i] != '1' and i % 2 == 1:
                answer += code[i]
            elif code[i] == '1':
                mode = 0
    return answer if answer else 'EMPTY'