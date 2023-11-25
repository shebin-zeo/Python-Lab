a=list(map(int,input('Enter list of number').split()))
b=int(input("Enter the number to be searched"))
print(a)
flag=0
count=0
for i in a:
      if i==b:
         count+=1
         flag=1
print('The item occure is',count)
if flag==0:
    print("Item not fount")

        
