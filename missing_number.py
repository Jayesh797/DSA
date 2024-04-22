def missing_num(list1,n):
    sum1=n*(n+1)/2
    sum2=0
    for i in list1:
        sum2=sum2+i

    return sum1-sum2

number_missing=missing_num([1,2,4,5],5)
print(number_missing)