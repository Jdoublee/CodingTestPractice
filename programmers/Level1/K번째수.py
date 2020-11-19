def solution(array, commands):
    answer = []
    
    for i, j, k in commands :
        i -= 1
        k -= 1
        arr = array[i:j]
        arr.sort()
        res = arr[k]
        answer.append(res)
    
    return answer