n=list(map(int,input('Enter the list of numbers').split()))
print("The list is",n)
j=0
for i in n:
    if i>100:
        n[j]='OVER'
    j=j+1
print(n)
        
