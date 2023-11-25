s=input("Enter the names with comma : ")
count=0
fname=s.split(',')
for name in fname:
            if name.lower().startswith("a"):
              count=count+1
print("The names start with a is : ",count)
              
