def matrix_zero(arr,m,n):
    col=[0]*m
    row=[0]*n
    for i in range(0,m):
        for j in range(0,n):
            if(arr[i][j]==0):
                row[i]=1
                col[j]=1
        
    for i in range(0,m):
        for j in range(0,n):
            if(col[j]==1 or row[i]==1):
                arr[i][j]=0
    
    return arr

arr=[
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1]
]



sd=matrix_zero(arr,4,4)

for i in range(0,4):
    for j in range(0,4):
        print(sd[i][j],end=" ")
    print()