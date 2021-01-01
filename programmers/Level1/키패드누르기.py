def getDistance(thumb, n):
    cod = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    d = 0
    n_i = [i for i in range(4) if cod[i][1] == n]

    if thumb not in (2, 5, 8, 11):
        d += 1

    for i in range(4):
        if thumb in cod[i]:
            d += abs(n_i[0] - i)
            break
    return d
            
            
def solution(numbers, hand):
    answer = ''
    
    l = 10
    r = 12
    
    for n in numbers:
        if n in (1, 4, 7):
            l = n
            answer += 'L'
        elif n in (3, 6, 9):
            r = n
            answer += 'R'
        else:
            if n == 0:
                n = 11
            left_d = getDistance(l, n)
            right_d = getDistance(r, n)
            
            if left_d == right_d:
                if hand == 'right':
                    r = n
                    answer += 'R'
                else:
                    l = n
                    answer += 'L'
            elif left_d < right_d:
                l = n
                answer += 'L'
            else:
                r = n
                answer += 'R'
    
    return answer
# 이런 문제는 단순 구현에 목표