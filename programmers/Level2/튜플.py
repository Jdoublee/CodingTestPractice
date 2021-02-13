def solution(s):
    answer = []
    
    li = []
    
    tup = s[1:-1].replace('{', '[').replace('}', ']').split('],')
    
    for x in tup:
        x = x.replace('[', '').replace(']', '')
        li.append(list(map(int, x.split(','))))
    
    li.sort(key=lambda x: len(x))
    
    for x in li:
        answer.extend(list(set(x) - set(answer)))

    return answer