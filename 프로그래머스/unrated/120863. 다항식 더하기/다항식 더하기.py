def solution(polynomial):
    answer = ''
    sum = 0
    num = 0
    polynomial = polynomial.replace(' ','').split('+') # 공백을 먼저 제거한 뒤에 + 기준으로 split
    for i in polynomial:
        if i[-1] == 'x': # print(i[-1]) # i[-1] -> x(변수)를 확인
            num += 1 if len(i) == 1 else int(i[:-1:])
        else:
            sum += int(i)
    if num > 0:
        answer = (str(num) if num > 1 else '') + 'x' + (' + ' if sum > 0 else '')
        
    answer += (str(sum) if sum > 0 else '')
    return answer