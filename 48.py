a=input("Enter the sentence")
count=0
for i in a:
    if i.lower() in 'aeiou':
        count+=1
print("Number of vowels : ",count)
