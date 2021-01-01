def solution(x):
    
    num = list(str(x))
    
    tot = 0
    
    for n in num:
        tot += int(n)
    
    if x % tot == 0:
        return True
    else:
        return False