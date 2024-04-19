def unique_elements(arr):
    i=0
    for j in range(1,len(arr)):
        if(arr[j]!=arr[i]):
            arr[i+1]=arr[j]
            i+=1
    return i+1

dc=unique_elements([1,1,2,2,2,2,3,4,5])
print(dc) 