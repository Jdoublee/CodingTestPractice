# def solution(gems):
        
#     names = list(set(gems))
    
#     l = 0
#     r = 0
    
#     cand = []
    
#     while 0 <= l < len(gems) and 0 <= r < len(gems) and l <= r:
#         check = {}

#         for name in names:
#             if name in gems[l:r+1]:
#                 check[name] = gems[l:r+1].count(name)
        
#         if len(check.keys()) < len(names):
#             r += 1
#         else:
#             if check[gems[l]] == 1:
#                 cand.append((l+1,r+1))
#             l += 1
    
#     cand.sort(key=lambda x:(x[1]-x[0],x[0]))
    
#     return cand[0]

# 11, 14 & 효율성 시간초과 코드

def solution(gems):
        
    names = set(gems)
    
    l = 0
    r = 0
    
    cand = []
    
    while l < len(gems):
        while r < len(gems):
            check = set(gems[l:r+1])

            if len(check) < len(names):
                r += 1
            else:
                cand.append((l+1,r+1))
                break
        l += 1
    
    cand.sort(key=lambda x:(x[1]-x[0],x[0]))
    
    return cand[0]

    # 정확성은 통과. 효율성은 6, 9 만 통과 코드.