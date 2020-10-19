# 1     1 	6 	14
# 2 	2 	7 	21
# 3 	4 	8 	22
# 4 	11 	9 	24
# 5 	12 	10 	41

def solution(n):
    answer = ''
    n = int(n)
    while True:
        if n%3==1:
            answer = '1' + answer
        elif n%3==2:
            answer = '2' + answer
        elif n!=0:
            answer = '4' + answer
            n //= 3
            n-=1
            continue
        else:
            break
        n //= 3
   
    return answer