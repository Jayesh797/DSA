# MOORE'S VOTING ALGORITHM

def Greater_than_n_by_2(arr):
    n=len(arr)
    ele=arr[0]
    cnt=1
    i=1
    while(i<n):
        if(cnt==0):
            ele=arr[i]
            cnt=1
        elif(ele==arr[i]):
            cnt+=1
        else:
            cnt-=1
        i+=1
    j=0
    cnt1=0
    while(j<n):
        if(arr[j]==ele):
            cnt1+=1
        j+=1
    if(cnt1>n//2):
        return ele
    else:
        return -1
    

arr=[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
sd=Greater_than_n_by_2(arr)
print(sd)