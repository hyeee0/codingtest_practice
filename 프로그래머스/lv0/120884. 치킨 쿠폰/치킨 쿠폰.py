def solution(chicken):
    answer = 0
    while chicken >= 10:
        a = chicken // 10
        answer += a
        chicken = chicken % 10 + a
    return answer