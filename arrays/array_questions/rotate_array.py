#first solve it with using temp variable means creating temporary array then return that array to original
# 1. Find the length n of the array.
# 2. Reduce k using k = k % n.
# 3. Create a temporary array to store the rotated values.
# 4. For every index i:
#        new_index = (i + k) % n
#        Put nums[i] at temporary[new_index].
# 5. Copy the temporary array back into nums.
def rotate_array(nums,k):
    n=len(nums)
    k=k%n
    # //create a temporary list with n positions
    temp=[0]*n             
    for i in range(len(nums)):
        # Calculate where the current element should go
        new_index=(i+k)%n 
        #place the element at its correct destination 
        temp[new_index]=(nums[i])
    #copy the rotated elements back into nums
    nums=temp
    #return that rotated list
    return nums
print(rotate_array([1,2,3,4,5,6,7,8],3))

#tc:O(n) //because only iterate 1 time through array thats why it is linear 
#sc:O(n) // beacuse we used temporaryy array to store values temporarily rather than doing in place rotations
