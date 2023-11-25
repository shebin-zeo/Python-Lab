characters=input("Enter characters\n")
charlist=characters.split(',')
string=""
for i in charlist:
    string=string+i
print("The string is",string)
print("".join(charlist))
