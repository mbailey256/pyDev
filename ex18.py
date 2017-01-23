



# exercise 18 Names, Variables, Code and Functions





# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2, arg3 = args
    print "arg1: %r, arg2: %r and arg3: %r" % (arg1, arg2, arg3)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one arguement
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw","Monkey")
print_two_again("Zeb","Shaw")
print_one("First!")
print_none()
