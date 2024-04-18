def find_second_largest(arr):
    max=arr[0]
    second_max=-1
    for i in range(0,len(arr)):
        if(arr[i]>max):
            second_max=max
            max=arr[i]
        elif(arr[i]<max and arr[i]>second_max):
                second_max=arr[i]
    return second_max

second_max=find_second_largest([2,3,1,4,7,7,5])
print(second_max)