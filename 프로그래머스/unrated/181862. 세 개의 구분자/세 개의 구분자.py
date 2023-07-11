def solution(myStr):
    import re
    answer = []
    answer = list(filter(None, re.split('[a|b|c]', myStr)))
    if answer == []:
        answer = ["EMPTY"]
    return answer