# "qno:1295"
# #find number with even number of digits    
# #approach 1 :convert int into string to use len
nums = [12,345,2,6,7896]
answer=0
for num in nums:
    digits=len(str(num))
    if digits%2==0:
        answer+=1
print(answer)        
#TC:0(n*d)
#SC:0(d)

#approach 2 where we divide that number repeatedly by 10
nums = [12,345,2,6,7896]
answer=0
for num in nums:
    digits=0
    while num>0:
        num=num//10
        digits+=1
    if digits%2==0:
        answer+=1
print(answer)

#tc:O(n*d)
#sc:0(1)

#approach 3:  use mathemantics range from 10-99 which has 2 digits,then 1000-9999 which has 4 digits  then 100000-999999 whic has 6 digits acoording to problem constraints which say the problem can only be valid to 10 to power 6 then use
#if statements and solve this approach


#approach 4: we have logarithmic function :
import math
digits=math.floor(math.log10(num))+1

#tc:O(n)
#sc:O(1)


