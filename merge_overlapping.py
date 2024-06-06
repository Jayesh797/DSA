def merge_overlapping(nums):
    nums=sorted(nums)
    nums2=[]
    for i in range(0,len(nums)):
        start=nums[i][0]
        end=nums[i][1]
        if(nums2 or start>nums[-1][-1]):
            nums2.append(nums[i])
        else:
            nums2[-1][-1]=max(nums2[-1][-1],end)
    return nums2

arr=[(1,3),(2,6),(8,9),(9,11),(8,10),(2,4),(15,18),(16,17)]
sd=merge_overlapping(arr)
print(sd)