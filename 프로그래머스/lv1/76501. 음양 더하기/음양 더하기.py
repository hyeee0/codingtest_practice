def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign == True:
            answer += absolute
        else:
            answer += absolute*(-1)
    return answer