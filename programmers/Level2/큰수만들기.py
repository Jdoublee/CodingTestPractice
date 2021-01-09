# 며칠을 고민한 문제
# 다시 봐두자
def solution(number, k):
    answer = []
    
    number = list(number)
        
    for i, n in enumerate(number):
        # answer에 원소가 존재하고(i=0인 경우엔 그냥 넣어주면 되니까 체크) 마지막 값이 현재 값보다 작으면 빼고 현재 값 넣어줌. k는 뺄 수 있는 값으로 남아있는지 체크.
        while len(answer) > 0 and answer[-1] < n and k > 0: 
            answer.pop() # 값 작으면 빼버림
            k -= 1 # 뺐다고 체크
        if k == 0: # 뺄 수 있는 값 더이상 없으면 그냥 남은 값 때려박음
            answer.extend(number[i:])
            break # 그리고 포문 탈출
        answer.append(n) # 현재 값보다 작은 애들 빼고나서 현재 값 추가
    
    if k > 0: # 빼야 할 값이 남았다면 현재 리스트에서 해당 개수만큼 뒤에서 빼줌
        answer = answer[:-k]
    
    return ''.join(answer) # 리스트 내 값들 join으로 문자열로 합쳐줌

# 앞에서부터 값 넣되 맨 뒤 값이랑 새로운 값이랑 비교 후 뺴주기
# 이미 들어있는 값들이 작으면 다 빼주고 값 넣기
# 스택/덱 도 사용해보기