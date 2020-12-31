def solution(arr):    
    
    if len(arr) == 1:
        arr = [-1]
    else:
        arr.remove(min(arr)) # min, max 잘 활용하기
    
    return arr