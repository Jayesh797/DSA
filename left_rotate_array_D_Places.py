import math
# def reverse(i,j,list1):
#     if(i<=j):
#         a=list1[i]
#         list1[i]=list1[j]
#         list1[j]=a
#         i+=1
#         j-=1
#         reverse(i,j,list1)
#     return list1

# list1=[1,2,3,4,5]
# k=3
# n=len(list1)
# reverse(0,k-1,list1)
# reverse(k,n-1,list1)
# reverse(0,n-1,list1)

# print(list1)

def reverse(i,j,arr):
    while(i<j):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1
    return arr

list1=[0,1,2,3,4,5,6,7]
k=3
n=len(list1)
reverse(0,k-1,list1)
reverse(k,n-1,list1)
arr1=reverse(0,n-1,list1)
print(arr1)
