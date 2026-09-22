#points:we use print instead of return because for return you have to create a lot of function again to again and to keep it simple we just used print 
#brute force of two sum:
#explain:we used two loops one store i means first index and other loops j staart from next index i+1 means contain next element from i then we check if value on index i + value of index j is equal to target then we return those indexes  

nums=[2,4,6,8,2]
target=8
answer=[]     #it is list used for storing indices of two values which sum is equal to target
for i in range(len (nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            answer=[i,j]
            print(answer)        

#tc:O(n*n)      //because we have two loops which are running n times means iterate untill everything done iterating
#sc:O(1)         //because we are not using any extra space thats why it is this(1)


#now we have better solution for this for better we use sorting +two pointers
nums = [2, 3, 8, 7, 3]
target = 9

answer = []

# Step 1: store value and original index
for i in range(len(nums)):
    answer.append((nums[i], i))

# Step 2: sort by value
answer.sort()

# Step 3: two pointers
left = 0
right = len(answer) - 1

while left < right:

    current = answer[left][0] + answer[right][0]

    if current == target:
        print([answer[left][1], answer[right][1]])
        break

    elif current < target:
        left += 1

    else:
        right -= 1

#tc:O(nlogn)               //because we use sorting here
# sc:O(n)                   //because we are using extra space If you create another data structure that can grow to the size of the input, its extra space is usually O(n).

#now we have optimal solution using hashmap: with dictionary
nums = [2, 3, 8, 7, 3]
target = 9
seen={}
for i in range(len(nums)):
    complement=target-nums[i]
    if complement in seen:
        print(seen[complement],i)
    seen[nums[i]]=i        
#tc:O(n)         //because we didnt use any extra things
#sc:O(n)           //because code is not takinga ny extra space 
