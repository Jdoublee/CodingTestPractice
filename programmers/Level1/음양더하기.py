def solution(absolutes, signs):
    res = 0
    
    for a,s in zip(absolutes,signs):
        if s:
            res += a
        else:
            res -= a
    
    return res