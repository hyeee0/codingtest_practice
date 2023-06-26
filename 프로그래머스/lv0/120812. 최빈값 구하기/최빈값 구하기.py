def solution(array):

    num_list = [] # 빈 리스트 선언
    set_array = list(set(array)) # 리스트 안에 중복값 제거
    
    for i in set_array:
        num_list.append(array.count(i))
        
    if num_list.count(max(num_list)) == 1:
        return set_array[num_list.index(max(num_list))]
    else:
        return -1