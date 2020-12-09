array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)) :
    for j in range(i, 0, -1) :
        if array[j-1] > array[j] : # 한 칸씩 왼쪽으로 이동
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break

print(array)
# O(N^2)
# 최선 : O(N) - 이미 정렬되어 있을 때