def solution(clothes):
    answer = 1
    
    dic = {}
    
    for d, c in clothes:
        if c not in dic.keys():
            dic[c] = [d]
        else:
            dic[c].append(d)
            
    for dk in dic.keys():
        answer *= len(dic[dk]) + 1 # 카테고리별로 0개~개수만큼 선택 가능. 각 카테고리별 가능한 수 다 곱해줌.
    # 적어도 하나의 의상은 입어야 하므로 모두 0개인 경우 1 빼줌
    answer -= 1

    return answer
    # 해시는 언제쯤 ^^