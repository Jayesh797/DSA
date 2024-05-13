def intersection_2_sorted_array(arr1,arr2):
    i=0
    j=0
    n1=len(arr1)
    n2=len(arr2)
    intersected_arr=[]
    while(i<n1 and j<n2):
        if(arr1[i]<arr2[j]):
            i+=1
        elif(arr1[i]==arr2[j]):
            intersected_arr.append(arr1[i])
            i+=1
            j+=1
        else:
            j+=1

    return intersected_arr

arr1=[1,2,2,3,3,4,5,6]
arr2=[2,3,3,5,6,6,7]
zc=intersection_2_sorted_array(arr1,arr2)
print(zc)