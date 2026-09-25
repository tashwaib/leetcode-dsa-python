#max consecutive ones
nums = [1,1,0,1,1,1]
count=0
max=0
for i in range(len(nums)):
    if nums[i]==1:
        count+=1
        if count>max:
            max=count
    else:
        count=0
print(max)                

 #tc:O(n)
 #sc:O(1)
