def solution(m, n, puddles):    
    ways = [[0 for _ in range(n)] for _ in range(m)] # 문제와 그림 예시가 달라서 혼란.. m행 n열이 맞다.
    
    ways[0][0] = 1 # 시작점만 1 부여
    
    for x, y in puddles:
        ways[x-1][y-1] = -1 # 물에 잠긴 지역 -1 처리
            
    for i in range(m):
        for j in range(n):
            if m==n==0: # 집 제외
                continue
                
            if ways[i][j] == -1: # 물웅덩이 제외
                continue

            # 위나 왼쪽 칸으로 이동해왔다면 두 값 더해줌(방법 추가)    
            if i-1 >= 0 and ways[i-1][j] != -1: # 위
                ways[i][j] += ways[i-1][j]
                
            if j-1 >= 0 and ways[i][j-1] != -1: # 왼쪽
                ways[i][j] += ways[i][j-1]
    
    # print(ways)
    
    return ways[-1][-1] % 1000000007 # 모듈러 연산 빼먹으면 효율성 0점 

    # 초등학교 수학 교과서에서 봤던 문제  ㅎ_ㅎ