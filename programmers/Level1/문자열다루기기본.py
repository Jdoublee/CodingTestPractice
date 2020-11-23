def solution(s):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(s) == 4 or len(s) == 6:
        for n in s :
            if n not in num :
                return False
        return True
    return False