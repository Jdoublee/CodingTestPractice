array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count_array = [0] * (max(array) + 1)

for i in range(len(array)) :
    count_array[array[i]] += 1

for i in range(len(count_array)) :
    for _ in range(count_array[i]) :
        print(i, end=' ')

# O(N+K) - K는 데이터 중 최대값의 크기