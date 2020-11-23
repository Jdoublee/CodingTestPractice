def solution(arr):
    answer = []
    i = 0
    for a in arr:
        if answer == [] :
            answer.append(a)
        elif answer[i] == a :
            continue
        else :
            answer.append(a)
            i += 1

    return answer