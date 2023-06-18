def solution(order):
    answer = 0
    americano = 4500
    cafelatte = 5000
    anything = 4500
    
    for i in order:
        if (i == 'americanoice') or (i == 'anything') or (i == 'iceamericano') or (i == 'hotamericano') or (i == 'americanohot') or (i == 'americano'):
            answer += 4500
        elif (i == 'icecafelatte') or (i == 'cafelatteice') or (i == 'hotcafelatte') or (i == 'cafelattehot') or (i == 'cafelatte'):
            answer += 5000
    return answer