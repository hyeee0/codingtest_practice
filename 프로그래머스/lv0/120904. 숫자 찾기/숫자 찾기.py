def solution(num, k):
    answer = -1
    num = str(num)
    k = str(k)
    a = list(num)
    for i in range(len(a)):
        print(a[i])
        if a[i] == k:
            print(a[i])
            answer = i + 1
            break
    return answer