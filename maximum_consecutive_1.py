def maximum_consecutive_1(arr):
    maxi=0
    cons=0
    for i in range(0,len(arr)):
        if(arr[i]==1):
            cons+=1
            if(cons>=maxi):
                maxi=cons
        else:
            cons=0
    return maxi

arr1=[1,1,0,1,1,1,0,0,1,1,1,1]
maxi=maximum_consecutive_1(arr1)
print(maxi)