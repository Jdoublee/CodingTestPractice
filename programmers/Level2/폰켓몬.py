def solution(nums):
    numset = set(nums)
    
    if len(numset) >= len(nums)//2:
        return len(nums)//2
    else:
        return len(numset)