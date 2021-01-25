def solution(s):
    stack = [] # stack 구조 활용

    for x in s:
        if len(stack) == 0: # 스택 비어있으면 그냥 push
            stack.append(x)
        else: # 스택 top 요소와 현재 값 비교
            if stack[-1] == x: # 같다면 pop
                stack.pop()
            else: # 다르면 현재 값 push
                stack.append(x)
                
    if stack: # stack에 값 남아있으면 실패
        return 0
    else: # 값 안 남아있으면 성공
        return 1