def reverse(s):
    '''Reverse a String'''
    if not len(s):return ' '
    else:return s[-1]+reverse(s[:-1])

s=input("Enter the string to reverse : ")
print("Reversed string is : ",reverse(s))
