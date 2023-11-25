s=input("Enter a string\n")
if(len(s)<2):
    new=''
elif (len(s)==2):
    new=s*2
else:
    new=s[:2]+s[-2:]
print(new)
