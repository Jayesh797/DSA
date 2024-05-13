def number_appearing_once_XOR(arr):
    xor=0
    for i in range(0,len(arr)):
        xor=xor^arr[i]
    return xor

arr1=[4,1,2,1,2,4,5]
a=number_appearing_once_XOR(arr1)
print(a)