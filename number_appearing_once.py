def number_appearing_twice(list1):
    maxi=0
    sumx=0
    for i in list1:
        sumx=sumx+i
        if(maxi<i):
            maxi=i

    sum1=maxi*(maxi+1)
    n=sum1-sumx
    return n

list1=[1,1,2,3,3,4,4]
number_once=number_appearing_twice(list1)
print(number_once)