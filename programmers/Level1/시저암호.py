def solution(s, n):
    answer = ''
    for ch in s :
        if ch == ' ' :
            answer += ch
            continue
        tmp = (ord(ch)+n)
        if (ord(ch) in range(65, 91) and tmp > 90) or (ord(ch) in range(97, 123) and tmp > 122): # 대문자 or 소문자 조건
            tmp -= 26
        answer += chr(tmp)
    return answer