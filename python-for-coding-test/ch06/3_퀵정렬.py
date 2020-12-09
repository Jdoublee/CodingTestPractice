# 가장 많이 사용되는 정렬 알고리즘
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end) :
    if start >= end :
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right :
        while left <= end and array[left] <= array[pivot] : # pivot보다 큰 값 찾을 때까지
            left += 1
        while right > start and array[right] >= array[pivot] : # pivot보다 작은 값 찾을 때까지
            right -= 1
        if left > right : # 엇갈렸다면, 작은 값과 피봇 swap
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[right], array[left] = array[left], array[right]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

def quick_sort2(array) :
    if len(array) <= 1 :
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort2(left) + [pivot] + quick_sort2(right)

print(quick_sort2(array))
# O(NlogN)
# 최악 : O(N^2) - 이미 정렬되어 있을 때