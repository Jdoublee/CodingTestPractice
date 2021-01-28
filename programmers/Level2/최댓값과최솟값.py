def solution(s):  
    nums = list(map(int, s.split()))
    
    nums.sort()
    
    return str(nums[0]) + ' ' + str(nums[-1])