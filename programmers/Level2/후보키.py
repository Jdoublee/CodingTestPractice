from itertools import combinations # 조합
def solution(relation):
    answer = 0
    
    col = len(relation[0])
    row = len(relation) 
    
    rem = [i for i in range(col)]
    
    res = []
    
    i = 1
    
    while i <= col:
        combs = list(combinations(rem, i)) # 가능한 조합 모두 구하기. 1개 ~ col개. -> 시간초과 안 나는 범위여서 가능
        
        for comb in combs:
            checklist = []

            # 최소성 체크
            flag = True 
            for r in res:
                if set(r) == set(comb).intersection(set(r)): # 부분집합 여부 판단. set 자료형이어야 함.
                    flag = False
                    break
            if not flag:
                continue
            
            for r in range(row):
                tmp = ''
                for c in comb:
                    tmp += relation[r][c]
                checklist.append(tmp)

            if len(set(checklist)) == row: # 유일성 체크
                answer += 1
                res.append(tuple(comb))
        i += 1
    
    return answer

# 다시 보기
# 풀이중 비트 연산 사용한 풀이 참고