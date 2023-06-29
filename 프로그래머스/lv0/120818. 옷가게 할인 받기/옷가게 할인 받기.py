def solution(price):
    answer = 0
    
    if 0 < price < 100000:
        answer = price
    elif 100000 <= price < 300000:
        answer = int(price - (price*0.05))
    elif 300000 <= price < 500000:
        answer = int(price - (price*0.1))
    elif 500000 <= price:
        answer = int(price - (price*0.2))
    
    return answer