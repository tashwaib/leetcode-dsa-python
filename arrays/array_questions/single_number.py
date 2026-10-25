#pseudocode for brute force approach using nested loops
# FUNCTION singleNumber(nums):
#     FOR each number in nums:
#         Set count = 0
#         FOR each other number in nums:
#             IF the two numbers are equal:
#                 Increase count by 1
#         IF count equals 1:
#             RETURN the number
def singlenumber(nums):
    for number in nums:
        count=0
        for i in range(len(nums)):
            if number==nums[i]:
                count+=1
        if count==1:
            return number            
print(singlenumber([1,2,1,1,2]))
# tc:o(n*n)//because nested loop has n*n time complexity in worst case
# sc:o(1)


