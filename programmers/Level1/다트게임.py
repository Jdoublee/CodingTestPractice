# 문제 주어진대로 구현
def mul(score, area):
    if area == 'S':
        return score
    elif area == 'D':
        return score ** 2
    else:
        return score ** 3


def solution(dartResult):    
    darts = list(dartResult)
    
    # print(darts)
    scores = []
    before = 0 # 1: num 2: bonus 3:option
    
    for dart in darts:
        if dart in '12345678910' and before != 1:
            scores.append(dart)
            before = 1
        elif dart == '0':
            tmp = scores.pop()
            scores.append(tmp+dart)
        elif dart in 'SDT':
            tmp = scores.pop()
            scores.append(mul(int(tmp), dart))
            before = 2
        elif dart == '*':
            if len(scores) > 1:
                tmp2 = scores.pop()
                tmp1 = scores.pop()
                scores.append(tmp1*2)
                scores.append(tmp2*2)
            else:
                scores[0] *= 2 
            before = 3
        else:
            tmp = scores.pop()
            scores.append(tmp *  -1)
            before = 3
            
    answer = sum(scores)
    
    return answer