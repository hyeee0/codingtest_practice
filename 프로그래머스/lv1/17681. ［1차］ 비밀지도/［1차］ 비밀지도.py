def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        binary = bin(arr1[i] | arr2[i]) # I : 비트논리 연산자 OR
        binary = binary[2:] # 앞에 2자리수 제거 -> print해보면 0b가 나오는데 0b제거하기 위해서~~~
        if n == len(binary): # n이랑 binary길이가 같으면 replace로 0은 공백으로 1은 #으로 바꾸고
            binary = binary.replace('0', ' ')
            binary = binary.replace('1','#')
            
        elif n > len(binary): # 이진법으로 변환했을 때 자리수가 n보다 작을 경우에
            padding = '0' * (n - len(binary)) # 부족한 길이만큼 '0'곱해준다
            binary = padding + binary # 앞에 채워주면 10진법으로 변환했을 때 값의 영향도 안주고, 길이가 n이랑 같아짐
            binary = binary.replace('0', ' ')
            binary = binary.replace('1', '#')
        answer.append(binary)
    return answer