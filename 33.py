mark=int(input("Enter percentage of mark\n"))

if(mark>=90):
    grade='A'
elif(mark>=80 and mark<90):
    grade='B'
elif(mark>=70 and mark<80):
    grade='C'
elif(mark>=60 and mark<70):
    grade='D'
else:
    grade='F'

print("Grade is :",grade)

