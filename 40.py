def sum(seq):
    '''Find sum of elements of a list'''
    if len(seq)==1:return seq[0]
    else:return seq[0]+sum(seq[1:])

l=[5,10,15,20,25]
print('Sum of elements of list',l,'=',sum(l))
