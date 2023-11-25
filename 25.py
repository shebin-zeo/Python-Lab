s=input("Enter the string")
if s.lower().endswith('ing'):
    s+='ly'
    print(s)
else:
    s+='ing'
    print(s)
