def solution(w,h):
    answer = 0
    
    for i in range(1, w):
        answer += (h * i) // w # 테케 12번 시간초과 남
    
    return answer * 2

# 동일 코드 C++로 하면 시간 초과따위 안 남^^
# 최대공약수로 어쩌구 저쩌구 풀라는데 내일 해보겠음