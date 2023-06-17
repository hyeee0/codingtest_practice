def solution(numbers):
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for i, j in enumerate(word):
 
        numbers = numbers.replace(j, str(i))

    return int(numbers)