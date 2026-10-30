def intersectionofarraytwo(nums1,nums2):
    count_items={}
    result=[]
    for number in nums1:
        if number in count_items:
            count_items[number]+=1
        else:
            count_items[number]=1
    for number in nums2:
        if number in count_items and count_items[number]>0:
            result.append(number)
            count_items[number]-=1
    return result
print(intersectionofarraytwo([5,5,7],[5,5,5,7]))

# For your Intersection of Two Arrays II dictionary approach:
# Time Complexity: \(O(n+m)\) — Average case
# Let's break it down:
# 1. First loop (nums1): \(O(n)\) — You visit every element and build the frequency dictionary.
# 2. Second loop (nums2): \(O(m)\) — You visit every element and check its frequency in the dictionary. Dictionary lookup and update take \(O(1)\) on average.
# Space Complexity: \(O(n+m)\)
# - Dictionary: \(O(n)\) worst case.
# - Result list: \(O(\min(n,m))\) worst case.
# So the combined auxiliary space is \(O(n+m)\).
# Time: \(O(n+m)\) average.
# Space: \(O(n+m)\) worst case, counting dictionary and result.

                      #second approach using sorting +two pointers
nums1=[1,2,2,1]
nums2=[2,2]
nums1.sort()
nums2.sort()
result=[]
i = 0
j = 0
while i < len(nums1) and j < len(nums2):
    if nums1[i]==nums2[j]:
        result.append (nums1[i])
        i+=1
        j+=1
    elif nums1[i]<nums2[j]:
        i+=1
    elif nums1[i]>nums2[j]:
        j+=1
print(result)
# #agr i chota hai tu i barhao aur j chota hai tu j barhao
# tc:O(nlogn+mlogm)
# sc:o(m+n) //Depends on sorting; O(n + m) worst case in Python

