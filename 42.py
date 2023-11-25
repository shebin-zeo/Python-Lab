def sum_n(n):
      '''Sum of N whole numbers'''
      if not n:return 0
      else:return n+sum_n(n-1)

n=int(input("Enter the number : "))
print('Sum of',n,'whole numbers = ',sum_n(n))
