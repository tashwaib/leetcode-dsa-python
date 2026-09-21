#solution for brute force code of this valid anagram question:
s="madam"
t="damam"
def valid_anagram():
    if len(s)!=len(t):
     return False
    sort_s=sorted(s)
    sort_t=sorted(t)
    if sort_s==sort_t:
       return True
    return False 

#solution for better it doesnt have better just brute force and optimal 


#optimal solution using hashmap dictionary
s="madam"
t="damam"
def valid_anagram():
    if len(s)!=len(t):
        return False
    countS={}
    countT={}
    for i in range(len(s)):
       countS[s[i]]=1+countS.get(s[i],0)     #this line just simply says get the first value from s string which is "s" and if you already seen it add 1 and give me that value with their frequency and if you didnt see it give me 0 means return 0
       countT[t[i]]=1+countT.get(t[i],0)
    return countS==countT
   



   
   