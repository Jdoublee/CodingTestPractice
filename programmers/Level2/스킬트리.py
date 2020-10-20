def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        li = []
        flag = -1
        for s in st:
            if s in skill:
                if skill.index(s)>len(li):
                    flag = 0
                    break
                elif skill.index(s)==len(li):
                    li.append(s)
        if flag == -1:
            answer += 1
        
    return answer