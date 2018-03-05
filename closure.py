# This closure usually is used in nested function

# A example for nested function 
def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")
# The result shows that the printer() can access to the outside function 



# Define a Closure Function 
def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    return printer  # this got changed

another = print_msg("Hello")
another()
# Output: Hello

# Now let's try calling this function.

#This value in the enclosing scope is remembered even when the variable goes out of scope 
#or the function itself is removed from the current namespace.


# When to use closures? 
# Closures can avoid use of global variables and provides some form of data hiding.
# It can also provide an object oriented solution to the problem	


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))


