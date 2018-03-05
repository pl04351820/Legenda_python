# *args and **kwargs is a common idiom to allow arbitary number of arguments to function as described.

# * args allow you all function parameters as a tuple
def foo(*args):
	for a in args:
		print (a)

# Here you can pass arbitary parameters.
foo(1)
foo(1,2,3)

# **kwargs give you all keyword arguments except for those corresponding to a formal parameteras
# as a dictionary
def bar(**kwargs):
	for a in kwargs:
		print (a, kwargs[a])

bar(name='one', age=27)

