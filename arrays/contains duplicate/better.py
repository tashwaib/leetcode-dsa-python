def containsduplicate(nums):
    nums=[2,4,9,0,4,0]
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            return True
        return False
        