import re
def solution(my_string):
    answer = 0
    a = re.findall('\d+', my_string)
    print(a)
    for i in range(len(a)):
        print(a[i])
        answer += int(a[i])
    return answer