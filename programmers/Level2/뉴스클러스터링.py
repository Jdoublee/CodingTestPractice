def solution(str1, str2):
    answer = 0
    
    word = 'abcdefghijklmnopqrstuvwxyz' # 오타 없나 두 번 확인하길
        
    one = []
    two = []
    
    str1 = str1.lower() # 대소문자 구별 안 하므로 소문자로 바꿔줌
    str2 = str2.lower()
    
    for i in range(len(str1)-1):
        if str1[i] in word and str1[i+1] in word:
            one.append(str1[i]+str1[i+1])
            
    for i in range(len(str2)-1):
        if str2[i] in word and str2[i+1] in word:
            two.append(str2[i]+str2[i+1])
    
    tot = 0 # 합집합
    its = 0 # 교집합
    
    for o in one:
        if o in two:
            its += 1
            two.remove(o)
        tot += 1
    tot += len(two)
        
    if tot == 0: # "E=M*C^2", "e=m*c^2" 의 경우 [], [] 이므로 0으로 나누기 불가능. 1 * 65536 = 65536 리턴
        return 65536

    answer = int(its / tot * 65536) # 정수부만 리턴
    
    return answer
# 하나 하면 문제를
# 둘 하면 잘 읽자 ^_ㅠ