def solution(s):

    def ispldr(l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        return s[l+1:r]
            
    
    if len(s) == 1: # TC 17번
        return 1
    
    pldr = ''
    for i in range(len(s)-1):
        pldr = max(pldr, ispldr(i,i+1), ispldr(i,i+2), key=len) # max 함수도 key 지정 가능

    return len(pldr)