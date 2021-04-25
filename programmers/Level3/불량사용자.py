from itertools import product # 데카르트 곱 - 두 개 이상의 리스트 조합

def solution(user_id, banned_id):    
    cand = [] # 제재 가능 아이디 리스트 저장
    
    for bid in banned_id:
        tmp = []
        for uid in user_id:
            if len(bid) != len(uid):
                continue
            i = 0
            while i < len(bid):
                if bid[i] == '*' or bid[i] == uid[i]:
                    i += 1
                else:
                    break
            if i == len(bid):
                tmp.append(uid)
        cand.append(tmp)
        
    pid = list(product(*cand)) # 각각의 제재 가능한 아이디 조합
    
    fid = set(tuple(sorted(list(d))) for d in dd if len(set(d)) == len(d)) # 조합 중 중복 없는 아이디 집합
    
    return len(fid)

# 테케 5번 : 7291.84ms, 1.91GB