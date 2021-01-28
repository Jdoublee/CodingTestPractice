def solution(n):
    nextnum = n + 1
    
    while True:
        if bin(nextnum).count('1') == bin(n).count('1'):
            return nextnum
            
        nextnum += 1