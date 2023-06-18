import numpy as np
import math
def solution(n):
    answer = -1
    a = np.sqrt(n)
    num = int(a)
    if a == num:
        answer = (num+1)**2
    return answer