def solution(myString, pat):
    answer = 0
    a = []
    b = ''
    for i in myString:
        if i == 'A':
            a.append('B')
        elif i == 'B':
            a.append('A')
        b = ''.join(a)
        if pat in b:
            answer = 1
    return answer