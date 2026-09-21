nums=[2,4,7,9,0,0]
def containduplicate(nums):
 hashset=set()
 for n in nums:
    if n in hashset:
        return True
    hashset.add(n)
 return False  
answer=containduplicate(nums)
print(answer) 