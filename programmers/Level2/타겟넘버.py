# +-숫자 를 자식 노드로 보고 트리 형태의 연산 구현
# 위처럼 생각하는게 어려웠다.
# 그림 그려서 참고할 예정
def solution(numbers, target):
    answer = 0
    node = [0]
    for n in numbers:
        tree = []
        for nd in node:
            tree.append(nd + n)
            tree.append(nd - n)
        node = tree
    # print(node.count(target))
    # print(len(node))
    
    answer = node.count(target)
    
    return answer