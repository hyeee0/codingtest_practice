def solution(my_string):
    answer = [0] * 52

    '''ord()함수는 문자를 해당하는 Unicode코드 포인트로 변환해주는 함수'''
    
    for str in my_string:
        if 'A' <= str <= 'Z':
            index = ord(str) - ord('A')
        elif 'a' <= str <= 'z':
            index = ord(str) - ord('a') + 26
        answer[index] += 1
    
    return answer