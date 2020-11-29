def solution(s):
    answer = ''
    words = s.split(' ') # split() 으로 하면 문자열 앞뒤의 공백이 삭제됨
    
    for w in words :
        first = w[::2].upper()
        second = w[1::2].lower()

        for i in range(len(second)) :
            answer += first[i]
            answer += second[i]
        if len(w) % 2 != 0 :
            answer += first[-1]
        answer += ' '
    
    return answer[:-1]