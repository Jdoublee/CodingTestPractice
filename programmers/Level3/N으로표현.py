def solution(N, number):    
    if N == number:
        return 1
    
    nset = [[] for _ in range(9)]
    
    # 5, 55, 555,... 등의 연속된 숫자 먼저 추가
    for i in range(1,9):
        nset[i].append(int(str(N)*i))
    
    # DP
    # nset[3] = nset[1]과 nset[2] 연산, nset[4] = nset[1]과 nset[3] 연산 + nset[2]와 nset[2] 연산 + nset[3]과 nset[1] 연산, ...
    for i in range(1,9):
        for j in range(i):
            for x in nset[j]:
                for y in nset[i-j]:
                    nset[i].append(x+y)
                    nset[i].append(x-y)
                    nset[i].append(x*y)
                    if y != 0:
                        nset[i].append(x//y)

        if number in nset[i]:
            return i    
    
    return -1