inputfile=False
try:
    inputfile=open("input.txt",'r+')
    inputf=inputfile.readlines()
    print(inputf)
    n=int(input("Enter line number to be removed\n"))
    inputf.pop(n-1)
    print("List after removing :",inputf)
    inputfile.truncate(0)
    inputfile.seek(0,0)
    inputfile.writelines(inputf)
    inputfile.seek(0,0)
    print(inputfile.read())
    
except Exception as e:
    print(e)
finally:
    if inputfile:inputfile.close()
