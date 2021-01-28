import numpy as np

def solution(arr1, arr2):
    a = np.array(arr1)
    b = np.array(arr2)
    
    c = np.matmul(a, b)
    
    return c.tolist()