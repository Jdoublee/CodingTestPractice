# 해시 사용법을 알아여겠다.
def solution(genres, plays):
    answer = []
    
    play = {} # 장르 순서 정하기 위한 딕셔너리 선언. 각 장르에 속한 곡들의 재생 수 합 순으로 장르 정렬.
    dic = {} # 재생 수랑 인덱스 저장. 각 장르 내에서 재생 수 순으로 정렬 후 앞에서 2개까지 잘라서 사용.
    
    for i in range(len(genres)):
        if genres[i] in dic.keys():
            play[genres[i]].append(plays[i])
            dic[genres[i]].append((plays[i], i))
        else:
            dic[genres[i]] = [(plays[i], i)]
            play[genres[i]] = [plays[i]]
    
    nn = sorted(play.items(), key=lambda p:sum(p[1]), reverse=True) # 장르를 재생수 합 기준으로 정렬.
    order = [v[0] for v in nn] # 튜플 형태로 리스트에 값 저장되 있으니 튜플의 첫번째 요소인 장르만 저장
    
    idx = {} # 정답으로 리턴할 인덱스 장르별 최대 두개씩 저장
    
    for k, v in dic.items():
        v.sort(reverse=True, key=lambda x:(x[0], -x[1])) # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다. 구현 위해 키 두개 설정.
        if len(v) < 2: # 장르에 속한 곡이 하나인 경우 따로 처리
            idx[k] = [v[0][1]]
        else:
            idx[k] = [v[0][1], v[1][1]]
            
    for g in order: # 장르 순서대로 answer에 추가
        answer.extend(idx[g]) # list 형태이므로 extend 사용
    
    return answer

# 다른 사람 풀이 참고해보기 : https://programmers.co.kr/learn/courses/30/lessons/42579/solution_groups?language=python3