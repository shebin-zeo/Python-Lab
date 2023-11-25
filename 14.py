a=input("Enter a string : ")
a=a.casefold()
rev=reversed(a)
if list(a)==list(rev):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
