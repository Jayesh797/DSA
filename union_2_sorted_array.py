def union_2_sorted_array(arr1,arr2):
    j=0
    i=0
    union_arr=[]
    n1=len(arr1)
    n2=len(arr2)
    while(i<n1 and j<n2):
        if(arr1[i]<arr2[j]):
            if(len(union_arr)==0 or union_arr[-1]!=arr1[i]):
                union_arr.append(arr1[i])
            i+=1
        else:
            if(len(union_arr)==0 or union_arr[-1]!=arr2[j]):
                union_arr.append(arr2[j])
            j+=1
    while(i<n1):
        if(len(union_arr)==0 or union_arr[-1]!=arr1[i]):
                union_arr.append(arr1[i])
                i+=1
    while(j<n2):
         if(len(union_arr)==0 or union_arr[-1]!=arr2[j]):
                union_arr.append(arr2[j])
                j+=1
    return union_arr

arr1=[1,1,2,2,3,4,5]
arr2=[1,2,2,3,3,4,4,5,6,7]
zc=union_2_sorted_array(arr1,arr2)
print(zc)
    