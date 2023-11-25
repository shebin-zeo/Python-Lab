def even_collection(l):
    for item in l:
         if(item==237):break
         elif not item%2:print(item)
n=input("Enter a collection of integers : ")
n=list(map(int,n.split()))
even_collection(n)
       
