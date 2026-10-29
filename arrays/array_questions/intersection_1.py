#intersection of two arrays 1
#pseudocode:
# CREATE an empty list called result

# FOR each number in the first array:
#     IF number exists in the second array:
#         IF number is not already in result:
#             ADD number to result
# RETURN result
def intersection(nums1, nums2):
    result = []

    # Check each number in the first array
    for number in nums1:

        # Check if the number also exists in the second array
        if number in nums2:

            # Avoid adding duplicate numbers to the result
            if number not in result:
                result.append(number)
    return result
print(intersection([1, 2, 2, 3], [2, 2, 4]))
# tc:O(n*m)
# sc:O(min(m,n))

#optimal solution using set
def intersectionoftwoarrays(nums1,nums2):
    new_set=set(nums1)
    result=[]
    for number in nums2:
        if number in new_set:
            result.append(number)
            new_set.remove(number)
    return result
print(intersectionoftwoarrays([1,2,3,4],[2,2,4,4]))
# tc:O(m+n)
# sc:O(m+n)    




        
