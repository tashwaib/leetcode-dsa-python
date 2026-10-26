# #pseudocode for brute force approach using nested loops
# # FUNCTION singleNumber(nums):
# #     FOR each number in nums:
# #         Set count = 0
# #         FOR each other number in nums:
# #             IF the two numbers are equal:
# #                 Increase count by 1
# #         IF count equals 1:
# #             RETURN the number
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
#better approach foer this problem is using dictionary:
def single_number(nums):
    count_dicts={}
    for number in nums:
        if number in count_dicts:
            count_dicts[number]+=1
        else:
            count_dicts[number]=1
    for number,count in count_dicts.items():
        if count==1:
            return number 
print(single_number([1,1,1,6,1]))
# # tc:o(n) //because we use one loop which search the count and then next loop just search in count for single number without running n times
# sc:o(n) //because we use extra memory 
#now optimal approach using bitwise operator:
def single_number(nums):
    result=0
    for number in nums:
        result=result^number
    return result
print(single_number([2,2,1]))  
# tc:o(n)      //its linear because we iterate only 1 times through array
# sc:o(1)      //beacsue we didnt use any extra space



