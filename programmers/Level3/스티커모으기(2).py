def solution(sticker):
    if len(sticker) < 3: # 1개 또는 2개인 경우
        return max(sticker)
    
    fdp = [0] * len(sticker)
    ldp = [0] * len(sticker)
    
    fdp[0] = sticker[0]
    fdp[2] = fdp[0]+sticker[2]
    
    ldp[1] = sticker[1]
    ldp[2] = max(sticker[1],sticker[2])
    
    for i in range(3,len(sticker)-1):
        fdp[i] = max(fdp[i-3]+sticker[i],fdp[i-2]+sticker[i],fdp[i-1])
    
    for i in range(3,len(sticker)):
        ldp[i] = max(ldp[i-3]+sticker[i],ldp[i-2]+sticker[i],ldp[i-1])
    
    return max(fdp[-2],ldp[-1])