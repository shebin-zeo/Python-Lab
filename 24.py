n1=input("Enter collection_1")
r=n1.split()
n2=input("Enter collection_2")
s=n2.split()
r1=set(map(int,r))
r2=set(map(int,s))
print (bool(len(r1)==len(r2)))
print (bool(sum(r1)==sum(r2)))
print (bool(len(r1&r2)))
        
 



