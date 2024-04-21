def revesearray_rec(n,i,list1):
    if(i>=n/2):
        return
    else:
        a=list1[i]
        list1[i]=list1[n-1-i]
        list1[n-i-1]=a
        revesearray_rec(n,i+1,list1)
        return list1

mylist=[1,2,3,4,5,6]
mylist2=revesearray_rec(6,0,mylist)
print(mylist)
