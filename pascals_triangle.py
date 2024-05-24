#PASCALS TRIANGLE

#type-1 print a value in given row and column
def print_val(r,c):
    ans=1
    for i in range(1,c+1):
        ans=ans*r
        ans=ans/i
        r-=1
    return ans

row=6
col=3
#print_val(row-1,col-1)
sd=print_val(row-1,col-1)
print(sd)

#type-2 print a complete row
def print_row(r):
    row_list=[]
    res=1
    row_list.append(res)
    for i in range(1,r):
        res=res*(r-i)
        res=res/i
        row_list.append(int(res))
    return row_list

sd=print_row(6)
print(sd)

#type-3 print a complete pascal triangle
def print_triangle(row):
    triangle_list=[]
    for i in range(1,row+1):
        row_i=print_row(i)
        triangle_list.append(row_i)

    return triangle_list

sd=print_triangle(6)
print(sd)
    
