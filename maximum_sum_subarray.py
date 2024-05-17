# KADANES ALGORITHM
def maximum_sum_subarray(arr):
    maxsum=arr[0]
    cursum=0
    i=0
    n=len(arr)
    while(i<n):
        cursum=cursum+arr[i]
        if(cursum>maxsum):
            maxsum=cursum
        if(cursum<0):
            cursum=0
        i+=1
    return maxsum

arr=[-2,-3,-1]
sd=maximum_sum_subarray(arr)
print(sd)