n = input()
n_li = [num for num in n]
n_li.sort(reverse=True) # 내림차순 정렬. default는 오름차순 정렬.

print(''.join(n_li))