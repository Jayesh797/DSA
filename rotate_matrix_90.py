def rotate_90(arr):
    r=len(arr)
    c=len(arr[0])
    for i in range(0,r-1):
        for j in range(i,r):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    
    for i in range(0,r):
        k=r-1
        j=0
        while(j<k):
            arr[i][j],arr[i][k]=arr[i][k],arr[i][j]
            j+=1
            k-=1
    return arr

arr=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
sd=rotate_90(arr)
for i in range(4):
    for j in range(4):
        print(sd[i][j],end=" ")
    print()