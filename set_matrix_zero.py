def setZeroes(matrix):
        r=len(matrix)
        c=len(matrix[0])
        row=[0]*r
        col=[0]*c
        for i in range(0,r):
            for j in range(0,c):
                if(matrix[i][j]==0):
                    row[i]=1
                    col[j]=1
        
        for i in range(0,r):
            for j in range(0,c):
                if(row[i]==1 or col[j]==1):
                    matrix[i][j]=0
        
        return matrix

arr=[
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1]
]



sd=setZeroes(arr)

for i in range(0,4):
    for j in range(0,4):
        print(sd[i][j],end=" ")
    print()