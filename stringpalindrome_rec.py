# method 1
def stringpalindrome_rec(string1):
    if(len(string1)<=1):
        return True
    if(string1[0]==string1[len(string1)-1]):
        return stringpalindrome_rec(string1[1:len(string1)-1])
    else:
        return False
    

print(stringpalindrome_rec("madama"))



