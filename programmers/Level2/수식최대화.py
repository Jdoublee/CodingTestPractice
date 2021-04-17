from copy import copy

def calc(a,b,op):
    if op =='+':
        return a+b
    elif op == '-':
        return a-b
    else:
        return a*b
    

def solution(expression):
    res = 0
    
    nums = expression.replace('-',' ').replace('+',' ').replace('*',' ')
    ops = []
    
    for i in range(len(nums)):
        if nums[i] == ' ':
            ops.append(expression[i]) # 연산자만 저장
    
    nums = list(map(int,nums.split())) # 숫자만 저장
    
    # print(nums)
    # print(ops)
    
    priority = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]] # 가능한 우선순위 경우 6가지
    
    for pr in priority:
        n = copy(nums)
        op = copy(ops)
        
        dic = {'+':pr[0], '-':pr[1], '*':pr[2]}
        
        pnum = 2 # 우선순위 큰거부터 계산
        while pnum >= 0:
            i = 0
            while i < len(op):
                if dic[op[i]] == pnum: # 해당 우선순위의 연산자이면
                    tmp = calc(n[i],n[i+1],op[i]) # 계산
                    n.insert(i,tmp) # 연산 후 해당 위치에 삽입 
                    n.pop(i+1) # 연산에 사용한 숫자, 연산자 삭제
                    n.pop(i+1)
                    op.pop(i)
                    # i는 그대로
                else:
                    i += 1
            pnum -= 1

        res = max(res,abs(n[0])) # 절댓갑 변환후 최대 비교 및 대입
    
    return res