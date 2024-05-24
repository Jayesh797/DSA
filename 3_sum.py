def sum_3(arr):
    result_arr=[]
    arr=sorted(arr)
    print(arr)
    for i in range(0,len(arr)):
        if(i>0 and arr[i]==arr[i-1]):
            continue
        j=i+1
        k=len(arr)-1
        while(j<k):
            sum=arr[i]+arr[j]+arr[k]
            if(sum<0):
                j+=1
            elif(sum>0):
                k-=1
            else:
                temp=[]
                temp.append(arr[i])
                temp.append(arr[j])
                temp.append(arr[k])
                result_arr.append(temp)
                j+=1
                k-=1
                while(arr[j]==arr[j-1] and j<k):
                    j+=1
                while(arr[k]==arr[k+1] and j<k):
                    k-=1
    
    return result_arr

arr=[2,2,0,-1,-2,-1,-1,0,-2,0,2,-2,2]
sd=sum_3(arr)
print(sd)