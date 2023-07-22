def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse = True) # 내름차순으로 정렬해주기
    for i in emergency:
        answer.append(sorted_emergency.index(i)+1)
    return answer