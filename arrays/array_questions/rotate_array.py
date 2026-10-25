# #first solve it with using temp variable means creating temporary array then return that array to original
# # 1. Find the length n of the array.
# # 2. Reduce k using k = k % n.
# # 3. Create a temporary array to store the rotated values.
# # 4. For every index i:
# #        new_index = (i + k) % n
# #        Put nums[i] at temporary[new_index].
# # 5. Copy the temporary array back into nums.
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

# #tc:O(n) //because only iterate 1 time through array thats why it is linear 
# #sc:O(n) // beacuse we used temporaryy array to store values temporarily rather than doing in place rotations
# #using cyclic rotations because prevoius approach will not work properly for short array length it might come backk to index 0 too quickly before completing all rotations.
# #pseudocode
# # 1. Find n, the array length.
# # 2. If n is 0, stop.
# # 3. Set k = k % n.
# # 4. Set moved = 0.
# # 5. While moved < n:
# #        Start a cycle at index start.
# #        current = nums[start]
# #        index = start

# #        Repeat:
# #            next_index = (index + k) % n

# #            Save nums[next_index] in a temporary variable.
# #            Put current into nums[next_index].
# #            current = the saved value.

# #            index = next_index
# #            moved = moved + 1

# #        Until index returns to start.

# #        Choose the next start index for another cycle,
# #        if some elements have not yet moved.
# #code:
def rotate_array(nums,k):
    n=len(nums)
    if n==0:
        return nums
    k=k%n
    start=0
    moved=0
    while moved<n:
        current=nums[start]
        current_index=start
    while True:
        new_index=(current_index+k)%n 
        temp=nums[new_index]
        nums[new_index]=current
        current=temp
        current_index=new_index
        moved=moved+1
        if current_index==start:
            break
    start=start+1
nums=[1,2,3,4,5,6,7]
rotate_array(nums,2)
print(nums)
# # 8. A useful memory trick
# # Remember these four steps:

# # CARRY → CALCULATE → SAVE → PLACE
# # 1. Carry the value we need to move.
# # 2. Calculate its destination using (index + k) % n.
# # 3. Save the value at that destination.
# # 4. Place the carried value there, then carry the saved value.
# # One more important detail: the number of separate cycles depends on the array length and k. Mathematically, it is related to \(\gcd(n,k)\), the greatest common divisor. You don't need to memorize that yet to implement the algorithm, but it explains why some rotations have one cycle while others have several.
# #contains duplicate brute force
def contains_duplicate(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    return False
print(contains_duplicate([1,2,3,1]))   
# tc:O(n*n)
# SC:O(1)
# #better solution:
# # we first sort it then compare it 
def contains_duplicate(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            return True
    return False
print(contains_duplicate([1,2,3,4,11,1,2,3])) 
# # tc:o(nlogn) // because we use sort 
# # sc:o(logn)   //because in memory sort conatins some extra space


                               #optimal approach usiing set from hashset
def contains_duplicate(nums):
    my_set=set()
    for i in nums:
        if i in my_set:
            return True
        my_set.add(i)
    return False
print(contains_duplicate([1,2,3,4,11,1,2,3]))    
# tc:o(n)
# sc:o(n)
