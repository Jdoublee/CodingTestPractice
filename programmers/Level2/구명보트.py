def solution(people, limit):
    cnt = 0
    people.sort()
    
    s = 0
    e = len(people) - 1
    
    while s <= e:
        if s == e:
            cnt += 1
            break
        
        if people[s] + people[e] <= limit: # index 비교가 아니라 remove, pop 등 리스트 요소를 변경하는 연산 수행시 효율성 통과 못 함. 빡빡한 문제.
            s += 1
        
        e -= 1
        cnt += 1

    return cnt
    # 리스트 연산은 느리니 덱이나 힙 사용하자