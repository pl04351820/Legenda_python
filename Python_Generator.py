
# Generator sometimes is better, since when do operation on a big list, the generator will consume less memory. The 
# Generator only save the algrithom, not save the list itself.

'''
The difference between Range and Xrange usually appears in python 2 
Range(5) creates a list [0,1,2,3,4]
xrange(5) creates a generator 

you should use the feature like list(xrange(5)) to see the list 
In Python3, xrange replace range and rename with range.
A feature
'''
a = range(1,5)
print (list(a))


'''
A sample of generator. Dynamic Processing
'''
L = [x * x for x in range(5)]
print (L)

g = (x * x for x in range(5))
print (g)

for i in g:
	print(i)