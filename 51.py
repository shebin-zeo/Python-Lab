def add(a):
    if a.startswith("ls"):
        return a
    else:
        return "ls"+a
s=input("Enter string : ")
print("New string : ",add(s))
