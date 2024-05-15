def longest_subaaray_with_given_sum(arr,k):
    left=0
    right=0
    n=len(arr)
    suma=arr[0]
    maxlen=0
    while(right<n):
        while(suma>k and left<right):
            suma=suma-arr[left]
            left+=1
        if(suma==k):
            maxlen=max(maxlen,right-left+1)
        right+=1
        if(right<n):
            suma=suma+arr[right]

    return maxlen
        
arr=[1,2,3,1,1,1,1,3,3]
maxlen=longest_subaaray_with_given_sum(arr,6)
print(maxlen)