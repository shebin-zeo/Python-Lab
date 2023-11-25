a=input("Enter a sentence :").split()
b=[i for i in a if len(i)==len(max(a,key=len))]
print("Repeting words are :",a)
if len(b)>1:
    print('Bingo')
