def sequential_search(n, target, array) :
    for i in range(n) :
        if array[i] == target :
            return i+1

n = 5
array = ['Red', 'Orange', 'Yellow', 'Green', 'Blue']
target = 'Yellow'

print(sequential_search(n, target, array))