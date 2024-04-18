def countfreq(n,M,arr):
    M=M+1
    hash = [0 for _ in range(M)]
    for i in range(0,n):
        hash[arr[i]]+=1
    return hash

dc=countfreq(6,15,[10,5,10,15,10,5])
max=0
min=100
for i in range(0,len(dc)):
    if(dc[i]>=max):
        max=dc[i]
    if(dc[i]<=min and dc[i]!=0):
        min=dc[i]
for j in range(0,len(dc)):
    if(dc[j]==max):
        max=j
    if(dc[j]==min):
        min=j

print(dc)
print('maximum number is: '+str(max))
print('minimum number is: '+str(min))