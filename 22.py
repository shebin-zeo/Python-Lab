letter={}
word=input("Enter the word")
for l in list(word):
 letter[l]=letter.get(l,0)+1
print(letter)
