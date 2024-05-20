def longest_consecutive_sequence(nums):
    nums=sorted(nums)
    i=1
    longest=1
    cnt=1
    maxi=nums[0]
    # maxi=-100
    while(i<len(nums)):
        if(nums[i]-1==maxi):
            cnt+=1
            maxi=nums[i]
        elif(nums[i]!=maxi):
            cnt=1
            maxi=nums[i]
        
        i+=1
    return longest

arr=[100,102,100,101,101,4,3,2,3,2,1,1,1,2]
sd=longest_consecutive_sequence(arr)
print(sd)
