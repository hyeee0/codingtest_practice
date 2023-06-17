def solution(bin1, bin2):
    answer = ''
    a = int(bin1, 2)
    b = int(bin2, 2)
    c = a + b
    c = bin(c)
    answer = c[2:]
    return answer