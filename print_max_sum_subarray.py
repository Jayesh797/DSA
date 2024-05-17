#KADANE'S ALGORITHM
def print_max_sum_subarray(arr):
    maxsum=arr[0]
    cursum=0
    i=0
    start=-1
    end=-1
    start_value=-1
    n=len(arr)
    while(i<n):
        if(cursum==0):
            start=i
        cursum=cursum+arr[i]
        if(cursum>maxsum):
            maxsum=cursum
            end=i
            start_value=start
        if(cursum<0):
            cursum=0
        i+=1
    max_arr=[]
    for j in range(start_value,end+1):
        max_arr.append(arr[j])
    
    return max_arr

arr=[-2,-3,4,-1,-2,1,5,-3]
sd=print_max_sum_subarray(arr)
print(sd)