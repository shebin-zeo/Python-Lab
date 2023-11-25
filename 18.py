words=input("Enter words\n")
wordlist=words.split()
number=int(input("Enter Number\n"))
for i in wordlist:
    if(len(i)>number):
        print(i)
