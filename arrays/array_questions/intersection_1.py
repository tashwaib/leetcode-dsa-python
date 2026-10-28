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