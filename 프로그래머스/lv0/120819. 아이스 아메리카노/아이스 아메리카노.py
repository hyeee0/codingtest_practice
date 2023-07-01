def solution(money):
    answer = []
    
    price = 5500 # 커피가격
    changes = 0 # 남은 잔돈
    coffee = 0 # 커피수

    if (money - (price * coffee)) == 0: # 잔돈이 발생하지 않을 때
        coffee += 1
    else:
        coffee = money // price 
        changes = money - (price * coffee)
        
        
    answer = [coffee, changes]    
    return answer