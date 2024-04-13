def countfreq(n,x,arr):
    hash = [0 for _ in range(11)]
    for i in range(0,n):
        hash[arr[i]]+=1
    return hash


dc=countfreq(6,9,[1,3,1,9,2,7])
print(dc)
