def arrange_array_element_by_sign(nums):
    i=0
    arr2 = [0] * len(nums)
    j=0
    k=1
    while(i<len(nums)):
        if(nums[i]>0):
            arr2[j]=nums[i]
            j+=2
        else:
            arr2[k]=nums[i]
            k+=2
        i+=1
    return arr2

nums=[3,1,-2,-5,2,-4]
sd=arrange_array_element_by_sign(nums)
print(sd)