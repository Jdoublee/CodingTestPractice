def solution(n, words):

    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return[i%n+1, i//n+1]

    return [0,0]