def solution(numbers):
    answer = []
    n = len(numbers)
    for i in range(n) :
        for j in range(i+1, n) :
            res = numbers[i] + numbers[j]
            answer.append(res)
    answer = list(set(answer))
    answer.sort()
    
    return answer