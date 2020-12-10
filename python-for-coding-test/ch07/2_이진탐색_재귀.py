def binary_search(array, target, start, end) :
    if start > end :
        return None
    mid = (start + end) // 2

    if array[mid] == target :
        return mid
    elif array[mid] < target :
        return binary_search(array, target, mid+1, end)
    else :
        return binary_search(array, target, start, mid-1)

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None :
    print('target 이 존재하지 않습니다.')
else :
    print(result+1, '에 존재')