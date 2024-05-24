def greater_n_by_3(arr):
    n=max(arr)
    hash=[0]*(n+1)
    result_array=[]
    for i in range(0,len(arr)):
        hash[arr[i]]=hash[arr[i]]+1
    x=len(arr)//3
    print(hash)
    for j in range(0,len(hash)):
        if(hash[j]>x):
            result_array.append(j)
        
    return result_array

arr=[1,1,1,3,2,2,2]
sd=greater_n_by_3(arr)
print(sd)