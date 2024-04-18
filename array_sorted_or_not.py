def check_array(arr):
    for i in range(1,len(arr)):
        if(arr[i-1]<=arr[i]):
            continue
        else:
            return False
        
pandu=check_array([1,2,3,4,3,6,7])
if(pandu==False):
    print("array is not sorted")
else:
    print("array is sorted")