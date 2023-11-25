a=input("Enter the strings seperated with space : ").split()
l=lambda a:[x for x in a if len(x)<5]
print(l(a))
