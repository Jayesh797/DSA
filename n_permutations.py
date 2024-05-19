def n_permutations(nums):
    n=len(nums)
    i=-1
    j=n-1
    while(j>=0):
        if(nums[j-1]<nums[j]):
            i=j-1
            break
        j-=1
    if(i==-1):
        nums2=sorted(nums)
        return nums2
    k=n-1
    while(k>=0):
        if(nums[k]>nums[i]):
            nums[k],nums[i]=nums[i],nums[k]
            break
        k-=1
    z=n-1
    s=i+1
    while(s<z):
        nums[s],nums[z]=nums[z],nums[s]
        s+=1
        z-=1
    
    return nums

arr=[3,2,1]
sd=n_permutations(arr)
print(sd)
    