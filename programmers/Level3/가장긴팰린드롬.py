# 효윻성 테스트 1 시간초과 :(
def ispalindrome(s):
    front = s[:len(s)//2]
    back = s[len(s)//2:]
    
    if len(s) % 2 == 1:
        back = back[1:]
    
    back.reverse()
    
    return front == back


def solution(s):    
    s = list(s)
    
    setlen = len(set(s))
    
    for i in range(len(s), 1, -1):
        j = 0
        while j+i <= len(s):
            subs = s[j:j+i]
            j += 1
            
            if ispalindrome(subs):
                return i
            # if subs == subs[::-1]:
            #     return i
    
    return 1