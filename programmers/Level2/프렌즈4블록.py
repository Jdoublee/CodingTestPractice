def solution(m, n, board):
    answer = 0
    res = []
    board = [list(b) for b in board] # 리스트 내 문자열도 리스트로 바꿔줌
        
    while True:
        for i in range(m-1):
            for j in range(1, n):
                # 2X2 영역 내 블록 다 같고 빈공간 아니라면 res 리스트에 추가. 
                if board[i][j-1] == board[i][j] and board[i+1][j-1] == board[i+1][j] and board[i][j] == board[i+1][j] and board[i][j] != 'z':
                    if [i, j-1] not in res: # 중복 여부 판단 후에
                        res.append([i, j-1])
                    if [i, j] not in res:
                        res.append([i, j])
                    if [i+1, j-1] not in res:
                        res.append([i+1, j-1])
                    if [i+1, j] not in res:
                        res.append([i+1, j])

        if len(res) == 0: # 더이상 지워질 블록 없으면 탈출
            break

        answer += len(res) # 지워진 블록 개수 추가

        for a, b in res:
            board[a][b] = 'z' # 2X2 지워지는 블록 소문자 z로 치환 -> 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다. 조건 존재 (테케 9번)
        
        for i in range(m-1, -1, -1): # 지워진 블록 있으면 남은 블록 밑으로 내려주는 작업
            for j in range(n):
                if board[i][j] == 'z':
                    for k in range(i, -1, -1):
                        if board[k][j] != 'z':
                            board[i][j], board[k][j] = board[k][j], board[i][j]
                            break
        
        res = []         
    
    return answer
    
    # 더럽군