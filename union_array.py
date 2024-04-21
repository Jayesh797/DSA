#arrays are sorted
def union(list1,list2):
    i=0
    j=0
    union_list=[]
    while(i<len(list1) and j<len(list2)):
        if(list1[i]<=list2[j]):
            if(len(union_list)==0 or union_list[-1]!=list1[i] ):
                union_list.append(list1[i])
            i+=1
        else:
            if(len(union_list)==0 or union_list[-1]!=list2[j]):
                union_list.append(list2[j])
            j+=1

    while(j<len(list2)):
        if(len(union_list)==0 or union_list[-1]!=list2[j]):
            union_list.append(list2[j])
        j+=1

    while(i<len(list1)):
        if(len(union_list)==0 or union_list[-1]!=list1[i]):
            union_list.append(list1[i])
        i+=1
    
    return union_list


list1=[1,1,2,3,4,4,5]
list2=[1,2,2,5,6,7,8,9,10]

union_list=union(list1,list2)

print(union_list)
        
    