def solution(seoul):
    for s in seoul :
        if s == 'Kim' :
            return '김서방은 {}에 있다'.format(seoul.index(s))