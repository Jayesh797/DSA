def charhashing(n,arr):
    M=27
    hash=[0 for _ in range(M)]
    for i in range(0,n):
        hash[ord(arr[i])-97]+=1
    return hash

array=charhashing(6,['a','d','r','s','b','a'])
print(array)

