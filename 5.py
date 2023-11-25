a=input('Enter the first string :')
b=input('Enter the second string :')
print("Before swap :",a,b)
a1=b[:1]+a[1:]
b1=a[:1]+b[1:]
print("After swap is :",a1," ",b1)
