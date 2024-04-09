import math

def check_palindrome(i, n, word):
    if i >= math.floor(n/2):
        return True
    elif word[i] != word[n-1-i]:
        return False
    else:
        return check_palindrome(i+1, n, word)

print(check_palindrome(0, 3, "MOM"))
