def zeroes_at_last(arr):
    j=-1
    for i in range(len(arr)):
        if(arr[i]==0):
            j=i
            break
    if(j==-1):
        return arr
    else:
        for i in range(j+1,len(arr)):
            if(arr[i]!=0):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                j+=1
        return arr
    

arr1=zeroes_at_last([1,2,3,1])
print(arr1)

    