s=input("Enter some elements : ")
s1=s.split()
dup=[ ]
[dup.append(i) for i in s1 if i not in dup]
print("The duplicate elements are : ",dup)
