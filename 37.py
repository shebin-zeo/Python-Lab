def count_string(s):
     count=0
     for item in s.split():
          if len(item)>1 and item[0]==item[-1]:
              count+=1
          return count

n=input("Enter a collection of string : ")
count_string(n)
