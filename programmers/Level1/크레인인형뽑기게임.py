# 문제 조건 잘 읽기
def solution(board, moves):
    answer = 0
    basket = []
    for m in moves :
        for i in range(len(board[0])) : # board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다. 
            if board[i][m-1] > 0:
                basket.append(board[i][m-1])
                board[i][m-1] = 0
                break
        if len(basket) >=2 :
            if basket[-1] == basket[-2] :
                del basket[-1]
                del basket[-1]
                answer += 2
    
    return answer