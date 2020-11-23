def solution(arr, divisor):
    answer = []
    for a in arr :
        if a % divisor == 0 :
            answer.append(a)
    if answer == [] :
        return [-1]
    answer.sort()
    return answer