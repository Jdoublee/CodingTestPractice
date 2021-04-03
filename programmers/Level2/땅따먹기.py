def solution(land):
    
    dp = [[0 for _ in range(len(land))] for _ in range(4)]
    
    dp[0][0] = land[0][0]
    dp[1][0] = land[0][1]
    dp[2][0] = land[0][2]
    dp[3][0] = land[0][3]
    
    for i in range(1,len(land)):
        dp[0][i] = max(dp[1][i-1], dp[2][i-1], dp[3][i-1]) + land[i][0]
        dp[1][i] = max(dp[0][i-1], dp[2][i-1], dp[3][i-1]) + land[i][1]
        dp[2][i] = max(dp[0][i-1], dp[1][i-1], dp[3][i-1]) + land[i][2]
        dp[3][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1]) + land[i][3]
        

    return max(dp[0][-1], dp[1][-1], dp[2][-1], dp[3][-1])