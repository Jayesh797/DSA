def max_1(list1):
    max=0
    count=0
    for i in list1:
        if(i==1):
            count+=1
            if(count>max):
                max=count
        else:
            count=0

    return max

list1=[1,1,0,1,1,1,0,1,1,1]
maximum_1=max_1(list1)
print(maximum_1)