def sum_4(arr,target):
    arr=sorted(arr)
    result_arr=[]
    for i in range(0,len(arr)):
        if(i>0 and arr[i]==arr[i-1]):
            continue
        for j in range(i+1,len(arr)):
            if(j>i+1 and arr[j]==arr[j-1]):
                continue
            k=j+1
            l=len(arr)-1
            while(k<l):
                x=arr[i]+arr[j]+arr[k]+arr[l]
                if(x<target):
                    k+=1
                elif(x>target):
                    l-=1
                else:
                    temp=[]
                    temp.append(arr[i])
                    temp.append(arr[j])
                    temp.append(arr[k])
                    temp.append(arr[l])
                    result_arr.append(temp)
                    k+=1
                    l-=1
                    while(arr[k]==arr[k-1] and k<l):
                        k+=1
                    while(arr[l]==arr[l+1] and k<l):
                        l-=1
    return result_arr

arr=[1,2,3,1,2,3,4,1,3,2,4,5,4,5]
sd=sum_4(arr,8)
print(sd)

        
            