# The python coroutine is some kind better than threads for following three reasons:
# 1. Thread need to do synchronization for protecting shared resource
# 2. The cost to create thread is big
# 3. The memory consume of thread is big(4MB)

# Coroutine is an extension to generators. 1KB consume per coroutine.
def my_coroutine():
	while True:
		received = yield 
		print("this is received", received)

foo = my_coroutine()
# the call to next is required to prepare for generator
next(foo)
foo.send('first')
foo.send('second')


# A real_time applicaiton
def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)

it = minimize()
next(it)            # Prime the generator
print(it.send(10))
print(it.send(4))
print(it.send(3))
print(it.send(-1))