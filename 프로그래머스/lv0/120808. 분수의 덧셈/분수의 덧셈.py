def solution(numer1, denom1, numer2, denom2):

    numer3 = (numer1 * denom2) + (numer2 * denom1)
    denom3 = denom1 * denom2

    num = 1
    max_num = max(numer3, denom3)
    
    for i in range(max_num, 0, -1):
        if (numer3 % i == 0) and (denom3 % i == 0):
            num = i
            break
    
    answer = [numer3/num, denom3/num]
    return answer