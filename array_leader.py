def array_leader(nums):
    maximum_on_right=-300
    n=len(nums)
    i=n-1
    nums2=[]
    while(i>=0):
        if(nums[i]>maximum_on_right):
            nums2.append(nums[i])
            maximum_on_right=nums[i]
        i-=1
    return nums2

arr=[1,22,12,0,3,6]
sd=array_leader(arr)
print(sd)