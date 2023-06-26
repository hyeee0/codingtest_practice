def solution(array):
    import numpy
    
    answer = 0
    array.sort()
    answer = numpy.median(array)
    return answer