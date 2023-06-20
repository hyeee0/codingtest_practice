def solution(phone_number):
    answer = ''
    star_num = (phone_number[:-4])
    star = (len(star_num) * '*')
    answer = star + phone_number[-4:]
    return answer