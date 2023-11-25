num=input("Enter a list of numbers seperated by space : ")
num_list=num.split()
num_list=[int(num)for num in num_list]

if len(num_list)>0:
     maximum=max(num_list)
     minimum=min(num_list)

print("The list is : ",num_list)
print("Maximum element is : ",maximum)
print("Minimum element is : ",minimum)
