s=input("Enter the number with comma : ")
s1=s.split(',')
s2=[int(i) for i in s1]
even=[i for i in  s2 if(i%2==0)]
print("The even numbers are : ",even)
