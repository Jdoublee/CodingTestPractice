# 이것도 여러 날 고민한 문제 (w/큰수만들기)
# 경우 나눠서 잘 생각해보기
def solution(name):
    answer = 0
    
    check = [] # A가 아닌 값. 조이스틱으로 바꿔줘야 할 값 저장.
    
    for i, n in enumerate(name):
        if n != 'A':
            check.append(i)

    if check[0] == 0: # 맨 첫번째 글자는 이동 없이 처리 가능하므로 빼줌
        check.pop(0)    
    
    for n in name: # A에서 원래 글자로 조정하는 횟수 먼저 저장
        answer += min(ord(n) - ord('A'), 26 - (ord(n) - ord('A'))) # A->Z , A->Z->B 중 최솟값 저장
        
    cnt = min(check[-1], len(name) - check[0]) # 앞에서부터 뒤로 이동, 뒤에서부터 앞으로 이동 중 최소 이동 횟수 저장
    
    for i in range(len(check)-1): # BBBAAAB와 같이 오른쪽으로 이동중 역으로 이동해서 처리하는게 더 빠른지 체크
        tmp = 2 * check[i] + len(name) - check[i+1]
        cnt = min(cnt, tmp) # 정/역방향과 중간에 이동전환 하는 방법 중 최소횟수 저장
    
    answer += cnt # 이동 횟수 더해줌

    return answer
# 이것도 다시 보기