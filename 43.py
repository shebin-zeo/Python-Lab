def sum_digits(n):
    if not(n//10):return n
    else:return(n%10)+sum_digits(n//10)

print('Sum = ',sum_digits(1234))
    
