def plus_one(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i]==9:
            digits[i]=0
        else:
            digits[i]=digits[i]+1
            return digits
    digits.insert(0,1)
    return digits
print(plus_one([9,9,9,9]))    
# tc:o(n)
# sc:o(1)    
#pseudocode for writing move zeros code using two pointer technique
# FUNCTION moveZeroes(nums):
#     SET position = 0
#     FOR each index i from 0 to length of nums - 1:
#         IF nums[i] is not equal to 0:
#             SET nums[position] = nums[i]
#             INCREASE position by 1
#     WHILE position is less than length of nums:
#         SET nums[position] = 
#         INCREASE position by 1
#     RETURN nums
# h [0, 1, 0, 3, 12]
def movezeros(nums):
    position=0
    for i in range(0,len(nums)):
        if nums[i]!=0:
            nums[position]=nums[i]
            position+=1
    while position<len(nums):
        nums[position]=0
        position+=1
    return nums
print(movezeros([14, 1, 0, 0, 3]))   
# tc:O(n)
# sc:o(1)
# Keep this distinction in your DSA notebook: two separate loops do not automatically mean O(n²). Here, they run one after another, not inside each other.       
