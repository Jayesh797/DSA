def find_second_smallest(arr):
    smallest=arr[0]
    ssmallest=10000
    for i in range(1,len(arr)):
        if(smallest>arr[i]):
            smallest=arr[i]
            ssmallest=smallest
        elif(arr[i]!=smallest and arr[i]<ssmallest):
            ssmallest=arr[i]
    return ssmallest

second_smallest=find_second_smallest([2,3,1,4,7,5])
print(second_smallest)

