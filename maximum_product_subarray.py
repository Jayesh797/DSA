def max_pro_subarray(nums):
    ans=-1000000
    prefix=1
    suffix=1
    for i in range(0,len(nums)):
        if(prefix==0):
            prefix=1
        if(suffix==0):
            suffix=1
        prefix=prefix*nums[i]
        suffix=suffix*nums[len(nums)-1-i]
        ans=max(ans,max(suffix,prefix))

    return ans

arr=[2,3,-1,4]
sd=max_pro_subarray(arr)
print(sd)