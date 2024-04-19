def rotate_array_by_1(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=temp
    return arr

    # for i in range(1,len(arr)):
    #     temp=arr[i-1]
    #     arr[i-1]=arr[i]
    #     arr[i]=temp
    # return arr


arr=rotate_array_by_1([1,2,3,4,5])
print(arr)